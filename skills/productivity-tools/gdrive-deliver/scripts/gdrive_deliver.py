#!/usr/bin/env python3
"""
Google Drive Delivery — Intelligent format selection.

Routes files to the correct upload method based on 3-tier classification:
  human → Google Doc (styled via Docs API)
  ai    → Raw .md file (text/markdown)
  both  → Raw .md file (well-formatted for Drive preview)
  raw   → Native MIME type (CSV, XLSX, PDF, etc.)

Wraps existing infrastructure in scripts/gdrive_upload.py.

Usage:
  python3 gdrive_deliver.py --file REPORT.md --folder-id <id>
  python3 gdrive_deliver.py --files *.md *.csv --folder-id <id> --format auto
  python3 gdrive_deliver.py --folder output/ --folder-id <id> --dry-run
"""

import os
import sys
import argparse
import fnmatch
from pathlib import Path

import yaml

# Import core upload functions from existing infrastructure
# Support both centralized skills vault AND project-specific installations
SKILL_DIR = Path(__file__).resolve().parent.parent
POSSIBLE_SCRIPT_DIRS = [
    SKILL_DIR.parent.parent / "scripts",  # Project-specific: skills/gdrive-deliver/../../scripts
    Path.home() / ".gemini" / "enora" / "scripts",  # Enora project
]

for script_dir in POSSIBLE_SCRIPT_DIRS:
    if (script_dir / "gdrive_upload.py").exists():
        sys.path.insert(0, str(script_dir))
        break
else:
    raise ImportError("Could not find gdrive_upload.py in any known location")

from googleapiclient.http import MediaFileUpload

from gdrive_upload import (
    get_services,
    upload_file,
    find_or_create_folder,
    share_file,
)


def upload_md_as_gdoc(drive, filepath: Path, folder_id: str, name: str = None) -> dict:
    """Upload .md as a native Google Doc using Google's built-in conversion.

    This lets Google handle markdown→Doc formatting (headings, bold, lists, tables)
    rather than manually building Docs API requests.
    """
    name = name or filepath.stem.replace("_", " ").replace("-", " ").title()
    meta = {
        "name": name,
        "mimeType": "application/vnd.google-apps.document",
        "parents": [folder_id],
    }
    media = MediaFileUpload(str(filepath), mimetype="text/markdown", resumable=True)
    result = drive.files().create(
        body=meta, media_body=media,
        fields="id,name,webViewLink", supportsAllDrives=True,
    ).execute()
    url = result.get("webViewLink", "")
    print(f"  Created Google Doc: {name}")
    print(f"    → {url}")
    return {"id": result["id"], "name": name, "url": url}

# --- Format Classification ---

EXTENSION_TIERS = {
    ".yaml": "ai", ".yml": "ai", ".json": "ai", ".py": "ai",
    ".sh": "ai", ".toml": "ai", ".ini": "ai", ".cfg": "ai",
    ".env": "ai",
    ".pdf": "raw", ".docx": "raw", ".pptx": "raw",
    ".csv": "raw", ".xlsx": "raw",
    ".png": "raw", ".jpg": "raw", ".jpeg": "raw", ".gif": "raw",
}

FILENAME_TIERS = {
    "REPORT": "human", "ANALYSIS": "human", "SUMMARY": "human",
    "BRIEF": "human", "UPDATE": "human", "PRESS": "human",
    "GUIDE": "both", "REFERENCE": "both", "PROFILES": "both", "DOCS": "both",
    "SKILL": "ai", "CLAUDE": "ai", "README": "ai",
    "CONFIG": "ai", "MANIFEST": "ai",
}


def load_format_rules():
    """Load configurable format overrides from YAML."""
    rules_path = SKILL_DIR / "config" / "format_rules.yaml"
    if rules_path.exists():
        with open(rules_path) as f:
            return yaml.safe_load(f) or {}
    return {}


def classify_by_rules(filepath: Path, rules: dict) -> str | None:
    """Check file against configurable override rules."""
    overrides = rules.get("overrides", {})
    filename = filepath.name

    for tier, patterns in overrides.items():
        if isinstance(patterns, list):
            for pattern in patterns:
                if fnmatch.fnmatch(filename, pattern):
                    return tier
    return None


def classify_content(content: str) -> str:
    """Analyze markdown content to determine format tier."""
    lines = content.split("\n")

    has_frontmatter = len(lines) > 0 and lines[0].strip() == "---"
    code_block_count = content.count("```")
    prose_lines = [
        l for l in lines
        if len(l) > 80 and not l.startswith(("#", "-", "|", "`", " "))
    ]

    if code_block_count > 6 and len(prose_lines) < 5:
        return "ai"
    elif len(prose_lines) > 10 and code_block_count < 3:
        return "human"
    elif has_frontmatter and code_block_count > 3:
        return "ai"
    else:
        return "both"


def classify_file(filepath: Path, rules: dict) -> str:
    """Determine the format tier for a file."""
    # 1. Check configurable rules first
    tier = classify_by_rules(filepath, rules)
    if tier:
        return tier

    # 2. Check extension
    ext = filepath.suffix.lower()
    if ext in EXTENSION_TIERS:
        return EXTENSION_TIERS[ext]

    # 3. Check filename patterns
    stem = filepath.stem.upper()
    for keyword, tier in FILENAME_TIERS.items():
        if keyword in stem:
            return tier

    # 4. For .md files, analyze content
    if ext == ".md":
        try:
            content = filepath.read_text(encoding="utf-8")
            return classify_content(content)
        except Exception:
            return "both"

    # 5. Default
    return "raw"


# --- Delivery ---

def deliver_file(drive, filepath: Path, folder_id: str, tier: str, dry_run: bool = False) -> list[dict]:
    """Upload a single file using the correct method for its tier.

    Returns a list of results (most tiers produce 1 result, 'both' produces 2).
    """
    results = []

    if dry_run:
        if tier == "both":
            print(f"  [DRY RUN] {filepath.name} → .md (AI) + Google Doc (human)")
        else:
            print(f"  [DRY RUN] {filepath.name} → {tier}")
        return [{"name": filepath.name, "tier": tier, "url": "(dry run)"}]

    if tier == "human":
        # Native Google conversion: markdown → properly formatted Google Doc
        result = upload_md_as_gdoc(drive, filepath, folder_id)
        results.append({"name": filepath.name, "tier": "human (Google Doc)", "url": result.get("url", ""), "id": result.get("id")})

    elif tier == "both":
        # Upload BOTH: raw .md for AI + Google Doc copy for humans
        md_result = upload_file(drive, filepath, folder_id)
        print(f"  Uploaded .md: {filepath.name}")
        results.append({"name": filepath.name, "tier": "both (.md for AI)", "url": md_result.get("url", ""), "id": md_result.get("id")})

        doc_name = filepath.stem.replace("_", " ").replace("-", " ").title()
        gdoc_result = upload_md_as_gdoc(drive, filepath, folder_id, name=doc_name)
        results.append({"name": f"{doc_name} (Google Doc)", "tier": "both (Google Doc for humans)", "url": gdoc_result.get("url", ""), "id": gdoc_result.get("id")})

    elif tier == "ai":
        result = upload_file(drive, filepath, folder_id)
        print(f"  Uploaded raw: {filepath.name}")
        results.append({"name": filepath.name, "tier": "ai (raw .md)", "url": result.get("url", ""), "id": result.get("id")})

    else:  # raw
        result = upload_file(drive, filepath, folder_id)
        results.append({"name": filepath.name, "tier": "raw", "url": result.get("url", ""), "id": result.get("id")})

    return results


def main():
    parser = argparse.ArgumentParser(description="Deliver files to Google Drive with intelligent format selection")
    parser.add_argument("--file", help="Single file to deliver")
    parser.add_argument("--files", nargs="+", help="Multiple files to deliver")
    parser.add_argument("--folder", help="Directory of files to deliver")
    parser.add_argument("--folder-id", required=True, help="Google Drive folder ID to deliver into")
    parser.add_argument("--format", choices=["auto", "human", "ai", "both", "raw"], default="auto",
                        help="Format tier (default: auto-classify)")
    parser.add_argument("--share", nargs="*", help="Email addresses to share with")
    parser.add_argument("--dry-run", action="store_true", help="Preview without uploading")
    args = parser.parse_args()

    rules = load_format_rules()

    # Collect files
    files = []
    if args.file:
        files.append(Path(args.file))
    if args.files:
        files.extend(Path(f) for f in args.files)
    if args.folder:
        folder_path = Path(args.folder)
        files.extend(sorted(f for f in folder_path.iterdir() if f.is_file()))

    if not files:
        parser.print_help()
        return

    # Resolve relative paths
    files = [f if f.is_absolute() else (PROJECT_ROOT / f) for f in files]
    files = [f for f in files if f.exists()]

    if not files:
        print("No valid files found.")
        return

    # Classify files
    deliveries = []
    for f in files:
        tier = args.format if args.format != "auto" else classify_file(f, rules)
        deliveries.append((f, tier))

    print(f"\nDelivering {len(deliveries)} file(s) to Drive folder {args.folder_id}")
    print(f"{'─' * 60}")

    if args.dry_run:
        print(f"\n{'File':<45} {'Format':<15}")
        print(f"{'─' * 45} {'─' * 15}")
        for filepath, tier in deliveries:
            print(f"{filepath.name:<45} {tier:<15}")
        print(f"\n(Dry run — nothing uploaded)")
        return

    # Initialize Drive services (only need drive, not docs API)
    drive, _ = get_services()

    # Determine sharing recipients
    share_emails = args.share or []
    if not share_emails:
        sharing_config = rules.get("sharing", {})
        share_emails = sharing_config.get("default_emails", [])

    # Upload each file
    results = []
    for filepath, tier in deliveries:
        try:
            file_results = deliver_file(drive, filepath, args.folder_id, tier)
            for result in file_results:
                results.append(result)

                # Share if emails configured
                if share_emails and result.get("id"):
                    for email in share_emails:
                        try:
                            share_file(drive, result["id"], email)
                        except Exception:
                            pass
        except Exception as e:
            print(f"  ERROR: {filepath.name} — {e}")
            results.append({"name": filepath.name, "tier": "ERROR", "url": str(e)})

    # Summary
    print(f"\n{'─' * 60}")
    print(f"Delivered {len([r for r in results if r['tier'] != 'ERROR'])} file(s)\n")
    for r in results:
        print(f"  {r['name']}")
        print(f"    Format: {r['tier']}")
        if r.get("url"):
            print(f"    Link:   {r['url']}")
        print()

    folder_url = f"https://drive.google.com/drive/folders/{args.folder_id}"
    print(f"Drive folder: {folder_url}")


if __name__ == "__main__":
    main()
