#!/usr/bin/env python3
"""
LinkedIn Profile Finder — bulk-discover LinkedIn profile URLs via Apify.
Uses harvestapi/linkedin-profile-search actor with automatic key pool rotation
across 6 free-tier accounts ($30/mo combined). Paid account excluded (reserved
for intent signal sprint).

Usage:
  # Single query
  python3 linkedin_finder.py --query "CISO cybersecurity Berlin" --max-items 100 --output results.jsonl

  # Batch mode with ICP-tagged queries
  python3 linkedin_finder.py --batch queries.json --output results.jsonl

  # URLs only
  python3 linkedin_finder.py --query "CTO fintech London" --max-items 50 --urls-only --output urls.txt

  # Check key pool status
  python3 linkedin_finder.py --pool-status

  # Reset exhausted keys (start of new month)
  python3 linkedin_finder.py --pool-reset

Key pool: Uses APIFY_API_TOKEN_0 through _5 + APIFY_API_TOKEN (free accounts).
Excludes: APIFY_API_TOKEN_PREMIUM and APIFY_API_TOKEN_SQUR_PAID (reserved).
"""

import argparse
import json
import math
import os
import ssl
import sys
import time
import urllib.request
import urllib.error

# macOS Python often lacks system certs — create unverified context as fallback
try:
    _SSL_CTX = ssl.create_default_context()
    urllib.request.urlopen("https://api.apify.com", timeout=5, context=_SSL_CTX)
except Exception:
    _SSL_CTX = ssl._create_unverified_context()

ACTOR_ID = "harvestapi~linkedin-profile-search"
BASE_URL = "https://api.apify.com/v2"
RESULTS_PER_PAGE = 25

# Import key pool from same directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apify_key_pool import ApifyKeyPool


def get_token():
    """Get token from key pool (free accounts only)."""
    pool = ApifyKeyPool()
    token = pool.get_key()
    if token:
        return token
    # Fallback to env var
    token = os.environ.get("APIFY_API_TOKEN_PREMIUM")
    env_paths = [".env", os.path.expanduser("~/.gemini/squr/.env")]
    for path in env_paths:
        if os.path.isfile(path):
            with open(path) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("APIFY_API_TOKEN_PREMIUM="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")
    print("ERROR: APIFY_API_TOKEN_PREMIUM not found in environment or .env", file=sys.stderr)
    sys.exit(1)


def api_request(url, data=None, method="GET"):
    headers = {"Content-Type": "application/json"}
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60, context=_SSL_CTX) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        err_body = e.read().decode() if e.fp else ""
        print(f"API error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)


def start_run(token, search_query, max_items):
    url = f"{BASE_URL}/acts/{ACTOR_ID}/runs?token={token}"
    payload = {
        "searchQuery": search_query,
        "maxItems": max_items,
        "scrapeProfiles": False,
    }
    result = api_request(url, data=payload, method="POST")
    run_data = result.get("data", {})
    run_id = run_data.get("id")
    dataset_id = run_data.get("defaultDatasetId")
    if not run_id:
        print(f"ERROR: Failed to start run. Response: {json.dumps(result)}", file=sys.stderr)
        sys.exit(1)
    return run_id, dataset_id


def wait_for_run(token, run_id, poll_interval=5, max_wait=600):
    url = f"{BASE_URL}/actor-runs/{run_id}?token={token}"
    elapsed = 0
    while elapsed < max_wait:
        result = api_request(url)
        status = result.get("data", {}).get("status")
        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            usage = result.get("data", {}).get("usageTotalUsd", 0)
            charged = result.get("data", {}).get("chargedEventCounts", {})
            return status, usage, charged
        time.sleep(poll_interval)
        elapsed += poll_interval
    print(f"ERROR: Run {run_id} did not complete within {max_wait}s", file=sys.stderr)
    return "TIMEOUT", 0, {}


def fetch_results(token, dataset_id, fields=None):
    url = f"{BASE_URL}/datasets/{dataset_id}/items?token={token}&limit=10000"
    if fields:
        url += f"&fields={','.join(fields)}"
    result = api_request(url)
    return result if isinstance(result, list) else []


def estimate_cost(max_items):
    pages = math.ceil(max_items / RESULTS_PER_PAGE)
    return pages * 0.10


def run_search(token, query, max_items, verbose=True):
    est = estimate_cost(max_items)
    if verbose:
        print(f"  Query: \"{query}\"")
        print(f"  Max items: {max_items} (~{math.ceil(max_items/RESULTS_PER_PAGE)} pages)")
        print(f"  Estimated cost: ${est:.2f}")

    run_id, dataset_id = start_run(token, query, max_items)
    if verbose:
        print(f"  Run started: {run_id}")

    status, usage, charged = wait_for_run(token, run_id)
    if verbose:
        print(f"  Status: {status} | Actual cost: ${usage:.3f} | Pages: {charged.get('search-page', 0)}")

    if status != "SUCCEEDED":
        print(f"  WARNING: Run {status}. Skipping.", file=sys.stderr)
        return []

    results = fetch_results(token, dataset_id)
    if verbose:
        print(f"  Profiles found: {len(results)}")
    return results


def deduplicate(results):
    seen = set()
    unique = []
    for r in results:
        url = r.get("linkedinUrl", "")
        if url and url not in seen:
            seen.add(url)
            unique.append(r)
    return unique


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Profile Finder via Apify (key pool)")
    parser.add_argument("--query", "-q", help="Single search query")
    parser.add_argument("--batch", "-b", help="Batch queries JSON file (plain or ICP-tagged)")
    parser.add_argument("--max-items", "-m", type=int, default=100, help="Max profiles per query (default: 100)")
    parser.add_argument("--output", "-o", help="Output file path (JSONL with ICP tags)")
    parser.add_argument("--urls-only", action="store_true", help="Output URLs only")
    parser.add_argument("--dry-run", action="store_true", help="Cost estimate only")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress")
    parser.add_argument("--pool-status", action="store_true", help="Show key pool status")
    parser.add_argument("--pool-reset", action="store_true", help="Reset exhausted keys")
    args = parser.parse_args()

    pool = ApifyKeyPool()

    if args.pool_status:
        pool.status()
        return

    if args.pool_reset:
        pool.reset()
        print("Key pool reset. All keys marked as available.")
        pool.status()
        return

    if not args.query and not args.batch:
        parser.error("Provide --query, --batch, --pool-status, or --pool-reset")

    token = pool.get_key()
    if not token:
        print("ERROR: No available Apify keys in pool. Run --pool-status to check.", file=sys.stderr)
        sys.exit(1)
    verbose = not args.quiet
    if verbose:
        print(f"Using key: {pool.get_key_name()}")

    queries = []
    if args.batch:
        with open(args.batch) as f:
            batch = json.load(f)
        for item in batch:
            q = item if isinstance(item, dict) else {"query": item}
            q.setdefault("maxItems", args.max_items)
            queries.append(q)
    else:
        queries.append({"query": args.query, "maxItems": args.max_items})

    total_est = sum(estimate_cost(q["maxItems"]) for q in queries)
    total_items = sum(q["maxItems"] for q in queries)

    if verbose:
        print(f"LinkedIn Profile Finder")
        print(f"  Queries: {len(queries)}")
        print(f"  Total max items: {total_items}")
        print(f"  Estimated total cost: ${total_est:.2f}")
        print()

    if args.dry_run:
        for i, q in enumerate(queries, 1):
            est = estimate_cost(q["maxItems"])
            print(f"  [{i}] \"{q['query']}\" — max {q['maxItems']} items — ~${est:.2f}")
        print(f"\n  TOTAL: ~${total_est:.2f}")
        return

    seen_urls = set()
    total_found = 0
    total_cost = 0.0
    keys_rotated = 0

    out_f = open(args.output, "w") if args.output else None

    for i, q_obj in enumerate(queries, 1):
        query_str = q_obj["query"]
        max_items = q_obj.get("maxItems", args.max_items)
        metadata = {k: v for k, v in q_obj.items() if k not in ("query", "maxItems")}

        if verbose:
            print(f"[{i}/{len(queries)}] \"{query_str}\"", end="", flush=True)

        results = run_search(token, query_str, max_items, verbose=False)

        # Check if we got zero results due to credit exhaustion
        if not results and i > 1:
            # Might be exhausted — try rotating key
            pool.mark_exhausted(token)
            pool.rotate()
            new_token = pool.get_key()
            if new_token and new_token != token:
                token = new_token
                keys_rotated += 1
                if verbose:
                    print(f" → KEY ROTATED to {pool.get_key_name()}", end="", flush=True)
                results = run_search(token, query_str, max_items, verbose=False)
            elif not new_token:
                if verbose:
                    print(" → ALL KEYS EXHAUSTED. Stopping.", flush=True)
                break

        # Deduplicate, tag with ICP metadata, write incrementally
        new_count = 0
        for r in results:
            url = r.get("linkedinUrl", "").rstrip("/").lower()
            if url and url not in seen_urls:
                seen_urls.add(url)
                tagged = {
                    "url": r.get("linkedinUrl"),
                    "name": f"{r.get('firstName', '')} {r.get('lastName', '')}".strip() or None,
                    "headline": r.get("headline"),
                    "location": r.get("location", {}).get("linkedinText"),
                    "connections": r.get("connectionsCount"),
                    **metadata,
                    "source_query": query_str,
                    "source": "apify_harvestapi",
                }
                new_count += 1
                if out_f:
                    if args.urls_only:
                        out_f.write(tagged["url"] + "\n")
                    else:
                        out_f.write(json.dumps(tagged, ensure_ascii=False) + "\n")

        total_found += new_count
        if verbose:
            print(f" → {len(results)} found, {new_count} new (total: {total_found:,})", flush=True)

        if out_f and i % 10 == 0:
            out_f.flush()

    if out_f:
        out_f.close()

    if verbose:
        print(f"\nTotal unique profiles: {total_found:,}")
        print(f"Keys rotated: {keys_rotated}")
        if args.output:
            print(f"Saved to: {args.output}")


if __name__ == "__main__":
    main()
