"""
Tavus Avatar Setup — Generic Persona Deployment Tool
Creates Tavus.io CVI personas from persona bible markdown files.

Usage:
    python3 setup_persona.py --persona-file path/to/persona.md   # Create one persona
    python3 setup_persona.py --persona-dir path/to/personas/     # Create all in directory
    python3 setup_persona.py --list                              # List existing personas
    python3 setup_persona.py --list-replicas                     # List available stock replicas
    python3 setup_persona.py --dry-run --persona-file ...        # Show payload without creating

Environment:
    TAVUS_API_KEY — Required. Set in .env or export directly.
    Default account: jorian@intrinsic.com.de

Part of: tavus-avatar-setup skill (AntiGravity shared skills)
"""

import json
import os
import re
import ssl
import sys
import urllib.request
import urllib.error
from pathlib import Path

try:
    import certifi
    SSL_CTX = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    SSL_CTX = ssl.create_default_context()

TAVUS_API_BASE = "https://tavusapi.com/v2"


def load_api_key():
    """Read TAVUS_API_KEY from environment or .env file in cwd."""
    key = os.environ.get("TAVUS_API_KEY")
    if key:
        return key

    # Search for .env in cwd and parents (up to 3 levels)
    cwd = Path.cwd()
    for parent in [cwd] + list(cwd.parents)[:3]:
        env_file = parent / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                line = line.strip()
                if line.startswith("TAVUS_API_KEY=") and not line.startswith("#"):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val

    print("ERROR: TAVUS_API_KEY not found. Set it in .env or export it.")
    sys.exit(1)


def tavus_request(api_key, method, endpoint, body=None):
    """Make a request to the Tavus API."""
    url = f"{TAVUS_API_BASE}{endpoint}"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, context=SSL_CTX) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"  API Error {e.code}: {error_body}")
        return None


def extract_tavus_json(md_path):
    """Extract the Tavus API JSON block from a persona bible markdown file (Section 8)."""
    content = md_path.read_text()

    match = re.search(
        r"## \d+\.\s*TAVUS PERSONA CONFIGURATION.*?```json\s*\n(.*?)```",
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not match:
        print(f"  WARNING: No Tavus JSON found in {md_path.name}")
        return {}

    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"  ERROR: Invalid JSON in {md_path.name}: {e}")
        return {}


def list_personas(api_key):
    """List all personas in the account."""
    result = tavus_request(api_key, "GET", "/personas")
    if not result:
        return

    personas = result.get("data", result.get("personas", []))
    if isinstance(personas, list):
        print(f"\nExisting personas ({len(personas)}):\n")
        for p in personas:
            pid = p.get("persona_id", "?")
            name = p.get("persona_name", "unnamed")
            replica = p.get("default_replica_id", "none")
            print(f"  {pid}  {name:40s}  replica: {replica}")
    else:
        print(f"\nResponse: {json.dumps(result, indent=2)}")
    print()


def list_replicas(api_key):
    """List all available replicas (stock + custom) in the account."""
    result = tavus_request(api_key, "GET", "/replicas")
    if not result:
        return

    replicas = result.get("data", result.get("replicas", []))
    if isinstance(replicas, list):
        print(f"\nAvailable replicas ({len(replicas)}):\n")
        for r in replicas:
            rid = r.get("replica_id", "?")
            name = r.get("replica_name", "unnamed")
            rtype = r.get("replica_type", "?")
            status = r.get("status", "?")
            print(f"  {rid}  {name:35s}  type: {rtype:10s}  status: {status}")
    else:
        print(f"\nResponse: {json.dumps(result, indent=2)}")
    print()


def sanitize_layers(payload):
    """Remove layers/fields that break Tavus when sent with empty values.

    Tavus treats empty strings and empty objects as intentional overrides,
    not as "use defaults". This strips known-dangerous empty fields so
    personas work reliably. Based on empirical comparison of working vs
    broken personas (2026-03-09).
    """
    layers = payload.get("layers", {})
    if not layers:
        return payload

    # Remove entire llm layer if it has empty base_url or api_key —
    # these cause Tavus to try using empty values instead of defaults
    llm = layers.get("llm", {})
    if llm:
        has_empty_critical = (
            llm.get("base_url", None) == ""
            or llm.get("api_key", None) == ""
        )
        has_empty_tools = llm.get("tools") == []
        if has_empty_critical or has_empty_tools:
            print("  SANITIZE: Removing llm layer (empty base_url/api_key/tools breaks pipeline)")
            del layers["llm"]

    # Remove tts_engine if set — let Tavus route to its default engine
    tts = layers.get("tts", {})
    if tts.get("tts_engine"):
        print(f"  SANITIZE: Removing tts.tts_engine='{tts['tts_engine']}' (let Tavus use default)")
        del tts["tts_engine"]

    # Remove empty voice_settings
    if tts.get("voice_settings") == {} or tts.get("voice_settings") == {"speed": "normal"}:
        print("  SANITIZE: Removing tts.voice_settings (default speed, let Tavus handle)")
        tts.pop("voice_settings", None)

    # Remove perception layer if it's just the default raven-1
    perception = layers.get("perception", {})
    if perception and perception.get("perception_model") == "raven-1":
        print("  SANITIZE: Removing perception layer (raven-1 is the default)")
        del layers["perception"]

    # Clean up empty tts layer after removals
    if not tts:
        layers.pop("tts", None)

    payload["layers"] = layers
    return payload


def create_persona(api_key, payload, dry_run=False):
    """Create a single persona via POST /v2/personas. Returns persona_id."""
    name = payload.get("persona_name", "unnamed")

    # Sanitize layers to prevent known pipeline-breaking patterns
    payload = sanitize_layers(payload)

    if dry_run:
        print(f"\n  [DRY RUN] Would create: {name}")
        print(f"  System prompt: {payload.get('system_prompt', '')[:150]}...")
        print(f"  Replica: {payload.get('default_replica_id', 'none')}")
        print(f"  Full payload:\n{json.dumps(payload, indent=2)}")
        return None

    print(f"\n  Creating: {name}...")
    result = tavus_request(api_key, "POST", "/personas", payload)

    if result:
        pid = result.get("persona_id") or result.get("data", {}).get("persona_id")
        if pid:
            print(f"  Created: {pid}")
            return pid

    print(f"  FAILED to create {name}")
    return None


def process_file(api_key, md_path, dry_run=False):
    """Process a single persona bible file."""
    slug = md_path.stem
    print(f"\nProcessing: {slug}")

    payload = extract_tavus_json(md_path)
    if not payload:
        return None

    # Clean up placeholder voice IDs
    tts = payload.get("layers", {}).get("tts", {})
    voice_id = tts.get("external_voice_id", "")
    if voice_id.startswith("[PLACEHOLDER") or not voice_id:
        tts.pop("external_voice_id", None)

    persona_id = create_persona(api_key, payload, dry_run=dry_run)

    if persona_id:
        return {
            "persona_id": persona_id,
            "persona_name": payload.get("persona_name"),
            "replica_id": payload.get("default_replica_id"),
            "slug": slug,
        }
    return None


def main():
    args = sys.argv[1:]

    dry_run = "--dry-run" in args
    list_only = "--list" in args
    list_reps = "--list-replicas" in args

    api_key = load_api_key()
    print(f"Tavus API connected (key: ...{api_key[-6:]})")

    if list_only:
        list_personas(api_key)
        return

    if list_reps:
        list_replicas(api_key)
        return

    # Determine persona files to process
    persona_files = []

    if "--persona-file" in args:
        idx = args.index("--persona-file")
        if idx + 1 < len(args):
            p = Path(args[idx + 1])
            if p.exists():
                persona_files = [p]
            else:
                print(f"ERROR: File not found: {p}")
                sys.exit(1)

    elif "--persona-dir" in args:
        idx = args.index("--persona-dir")
        if idx + 1 < len(args):
            d = Path(args[idx + 1])
            if d.is_dir():
                persona_files = sorted(d.glob("*.md"))
                persona_files = [f for f in persona_files if not f.name.startswith("_")]
            else:
                print(f"ERROR: Directory not found: {d}")
                sys.exit(1)

    if not persona_files:
        print("Usage:")
        print("  python3 setup_persona.py --persona-file path/to/persona.md")
        print("  python3 setup_persona.py --persona-dir path/to/personas/")
        print("  python3 setup_persona.py --list")
        print("  python3 setup_persona.py --list-replicas")
        print("  Add --dry-run to preview without creating")
        sys.exit(0)

    print(f"\nFound {len(persona_files)} persona file(s):")
    for f in persona_files:
        print(f"  - {f.name}")

    # Process
    results = {}
    for md_path in persona_files:
        result = process_file(api_key, md_path, dry_run=dry_run)
        if result:
            results[result["slug"]] = result

    # Save results
    if results and not dry_run:
        output_dir = persona_files[0].parent
        output_file = output_dir / "_tavus_persona_ids.json"

        # Merge with existing if present
        existing = {}
        if output_file.exists():
            try:
                existing = json.loads(output_file.read_text())
            except json.JSONDecodeError:
                pass

        existing.update({k: {kk: vv for kk, vv in v.items() if kk != "slug"} for k, v in results.items()})

        with open(output_file, "w") as f:
            json.dump(existing, f, indent=2)
        print(f"\nPersona IDs saved to {output_file}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY: {len(results)}/{len(persona_files)} personas created")
    print(f"{'=' * 60}")
    for slug, info in results.items():
        print(f"  {info['persona_name']:40s}  {info['persona_id']}")


if __name__ == "__main__":
    main()
