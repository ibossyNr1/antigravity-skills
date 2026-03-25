#!/usr/bin/env python3
"""
LinkedIn Profile Finder via DuckDuckGo Search.
Finds LinkedIn profile URLs by searching site:linkedin.com/in with ICP criteria.
Completely free — no API key, no TOS, no setup.

~27 profiles per query. 50K profiles ≈ 1,850 queries ≈ $0.

Usage:
  python3 linkedin_ddg.py -q "CISO cybersecurity Berlin" -o results.jsonl
  python3 linkedin_ddg.py -b queries.json -o results.jsonl --delay 2
  python3 linkedin_ddg.py -b queries.json --dry-run
  python3 linkedin_ddg.py -b queries.json --urls-only -o urls.txt
"""

import argparse
import json
import os
import sys
import time

try:
    from ddgs import DDGS
except ImportError:
    print("Installing ddgs...", file=sys.stderr)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "ddgs"])
    from ddgs import DDGS

MAX_RESULTS_PER_QUERY = 30
AVG_PROFILES_PER_QUERY = 25


def search_ddg(query, max_results=30):
    """Search DuckDuckGo for LinkedIn profiles."""
    search_query = f"site:linkedin.com/in {query}"
    try:
        raw = list(DDGS().text(search_query, max_results=max_results))
        if not raw:
            # DDG sometimes returns empty — not an error, just no results for this query
            return "EMPTY", []
    except Exception as e:
        err = str(e).lower()
        if "ratelimit" in err or "429" in err or "too many" in err:
            return "RATE_LIMITED", []
        if "no results" in err:
            return "EMPTY", []
        print(f"  Search error: {e}", file=sys.stderr)
        return "ERROR", []

    results = []
    for r in raw:
        url = r.get("href", "").split("?")[0]
        if "linkedin.com/in/" not in url:
            continue
        title = r.get("title", "")
        name = title.split(" - ")[0].split(" | ")[0].strip() if title else None
        results.append({
            "url": url,
            "name": name if name and name != "LinkedIn" and len(name) < 60 else None,
            "title": title,
            "snippet": r.get("body", "")[:200],
        })

    return "OK", results


def main():
    parser = argparse.ArgumentParser(description="LinkedIn Profile Finder via DuckDuckGo (free)")
    parser.add_argument("--query", "-q", help="Single search query")
    parser.add_argument("--batch", "-b", help="Batch queries JSON file (plain strings or structured)")
    parser.add_argument("--output", "-o", help="Output file path")
    parser.add_argument("--urls-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--delay", type=float, default=2.0,
                        help="Delay between queries in seconds (default: 2.0)")
    parser.add_argument("--max-per-query", type=int, default=30,
                        help="Max results per query (default: 30)")
    args = parser.parse_args()

    if not args.query and not args.batch:
        parser.error("Provide --query or --batch")

    verbose = not args.quiet

    # Load queries
    queries = []
    if args.batch:
        with open(args.batch) as f:
            raw = json.load(f)
        for item in raw:
            if isinstance(item, dict):
                queries.append(item)
            else:
                queries.append({"query": item})
    else:
        queries.append({"query": args.query})

    est_profiles = len(queries) * AVG_PROFILES_PER_QUERY
    est_time_min = len(queries) * args.delay / 60

    if verbose:
        print(f"LinkedIn Profile Finder (DuckDuckGo — FREE)")
        print(f"  Queries: {len(queries)}")
        print(f"  Cost: $0.00")
        print(f"  Expected profiles: ~{est_profiles:,}")
        print(f"  Estimated time: ~{est_time_min:.0f} min")
        print()

    if args.dry_run:
        for i, q in enumerate(queries[:20], 1):
            qs = q["query"] if isinstance(q, dict) else q
            meta = ""
            if isinstance(q, dict) and "persona" in q:
                meta = f" [{q['persona']} | {q.get('industry','')} | {q.get('location','')}]"
            print(f"  [{i}] \"{qs}\"{meta}")
        if len(queries) > 20:
            print(f"  ... and {len(queries) - 20} more")
        print(f"\n  TOTAL: $0.00 | ~{est_profiles:,} profiles | ~{est_time_min:.0f} min")
        return

    # Execute searches with incremental write
    seen_urls = set()
    total_found = 0
    searches_done = 0
    rate_limited_count = 0
    consecutive_errors = 0

    out_f = open(args.output, "w") if args.output else None

    for i, q_obj in enumerate(queries, 1):
        query_str = q_obj["query"] if isinstance(q_obj, dict) else q_obj
        metadata = {k: v for k, v in q_obj.items() if k != "query"} if isinstance(q_obj, dict) else {}

        if verbose:
            print(f"[{i}/{len(queries)}] \"{query_str}\"", end="", flush=True)

        status, results = search_ddg(query_str, args.max_per_query)
        searches_done += 1

        if status == "RATE_LIMITED":
            rate_limited_count += 1
            consecutive_errors += 1
            for wait in [30, 60, 120, 300]:
                if verbose:
                    print(f" → RATE LIMITED, waiting {wait}s...", flush=True)
                time.sleep(wait)
                status, results = search_ddg(query_str, args.max_per_query)
                searches_done += 1
                if status != "RATE_LIMITED":
                    consecutive_errors = 0
                    break
            if status == "RATE_LIMITED":
                if verbose:
                    print(" → Still limited after 5min. Stopping.", flush=True)
                break
        elif status == "EMPTY":
            # No results for this query — normal, not an error
            if verbose:
                print(" → 0 results (query too specific)", flush=True)
            if i < len(queries):
                time.sleep(args.delay)
            continue
        elif status == "ERROR":
            consecutive_errors += 1
            if verbose:
                print(f" → ERROR ({consecutive_errors}/10), skipping", flush=True)
            if consecutive_errors >= 10:
                if verbose:
                    print("  10 consecutive errors. Stopping.", flush=True)
                break
            time.sleep(args.delay * 3)
            continue
        else:
            consecutive_errors = 0

        # Deduplicate and tag
        new_count = 0
        for r in results:
            url = r.get("url", "").rstrip("/").lower()
            if url and url not in seen_urls:
                seen_urls.add(url)
                tagged = {**r, **metadata, "source_query": query_str}
                new_count += 1
                if out_f:
                    if args.urls_only:
                        out_f.write(r["url"] + "\n")
                    else:
                        out_f.write(json.dumps(tagged, ensure_ascii=False) + "\n")

        total_found += new_count
        if verbose:
            print(f" → {len(results)} found, {new_count} new (total: {total_found:,})", flush=True)

        if out_f and i % 10 == 0:
            out_f.flush()

        if i < len(queries):
            time.sleep(args.delay)

    if out_f:
        out_f.close()

    if verbose:
        print(f"\nTotal unique profiles: {total_found:,}")
        print(f"Searches used: {searches_done}")
        print(f"Cost: $0.00")
        if rate_limited_count:
            print(f"Rate limits hit: {rate_limited_count}")
        if args.output:
            print(f"Saved to: {args.output}")


if __name__ == "__main__":
    main()
