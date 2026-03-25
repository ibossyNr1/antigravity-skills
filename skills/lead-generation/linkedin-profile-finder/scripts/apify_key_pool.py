#!/usr/bin/env python3
"""
Apify API key pool — rotates across multiple free-tier accounts to maximize credits.
Excludes the paid SQUR account (reserved for intent signal sprint).

Usage:
    from apify_key_pool import ApifyKeyPool
    pool = ApifyKeyPool()
    key = pool.get_key()       # get next available key
    pool.mark_exhausted(key)   # mark key when credits run out
    key = pool.get_key()       # automatically rotates to next
"""

import json
import os
import ssl
import urllib.request
import urllib.error

# SSL fix for macOS
try:
    _SSL_CTX = ssl.create_default_context()
    urllib.request.urlopen("https://api.apify.com", timeout=5, context=_SSL_CTX)
except Exception:
    _SSL_CTX = ssl._create_unverified_context()

# Keys to EXCLUDE from the pool (reserved for other purposes)
EXCLUDED_KEYS = {"APIFY_API_TOKEN_PREMIUM", "APIFY_API_TOKEN_SQUR_PAID"}

# Key names in priority order (free accounts first)
FREE_KEY_NAMES = [
    "APIFY_API_TOKEN_0",
    "APIFY_API_TOKEN_1",
    "APIFY_API_TOKEN_2",
    "APIFY_API_TOKEN_3",
    "APIFY_API_TOKEN_4",
    "APIFY_API_TOKEN_5",
    "APIFY_API_TOKEN",
]


class ApifyKeyPool:
    def __init__(self, env_paths=None):
        self.env_paths = env_paths or [
            ".env",
            os.path.expanduser("~/.gemini/squr/.env"),
        ]
        self.keys = self._load_keys()
        self.exhausted = set()
        self.current_index = 0
        self.state_file = os.path.expanduser("~/.cache/apify-key-pool-state.json")
        self._load_state()

    def _load_keys(self):
        """Load all free-tier Apify keys from .env files."""
        env_vars = {}
        for path in self.env_paths:
            if os.path.isfile(path):
                with open(path) as f:
                    for line in f:
                        line = line.strip()
                        if "=" in line and not line.startswith("#"):
                            key, _, val = line.partition("=")
                            key = key.strip()
                            val = val.strip().strip('"').strip("'")
                            if key.startswith("APIFY_API_TOKEN") and key not in EXCLUDED_KEYS:
                                env_vars[key] = val

        # Also check environment variables
        for name in FREE_KEY_NAMES:
            val = os.environ.get(name)
            if val and name not in EXCLUDED_KEYS:
                env_vars[name] = val

        # Order by priority
        ordered = []
        seen_vals = set()
        for name in FREE_KEY_NAMES:
            if name in env_vars and env_vars[name] not in seen_vals:
                ordered.append({"name": name, "token": env_vars[name]})
                seen_vals.add(env_vars[name])

        return ordered

    def _load_state(self):
        """Load exhausted key state from disk."""
        if os.path.isfile(self.state_file):
            try:
                with open(self.state_file) as f:
                    state = json.load(f)
                self.exhausted = set(state.get("exhausted", []))
                self.current_index = state.get("current_index", 0)
            except Exception:
                pass

    def _save_state(self):
        """Save exhausted key state to disk."""
        os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
        with open(self.state_file, "w") as f:
            json.dump({
                "exhausted": list(self.exhausted),
                "current_index": self.current_index,
            }, f)

    def get_key(self):
        """Get the next available (non-exhausted) key token."""
        available = [k for k in self.keys if k["name"] not in self.exhausted]
        if not available:
            return None
        idx = self.current_index % len(available)
        return available[idx]["token"]

    def get_key_name(self):
        """Get the name of the current key."""
        available = [k for k in self.keys if k["name"] not in self.exhausted]
        if not available:
            return None
        idx = self.current_index % len(available)
        return available[idx]["name"]

    def rotate(self):
        """Move to the next key in the pool."""
        self.current_index += 1
        self._save_state()

    def mark_exhausted(self, token=None, name=None):
        """Mark a key as exhausted (credits used up)."""
        if name:
            self.exhausted.add(name)
        elif token:
            for k in self.keys:
                if k["token"] == token:
                    self.exhausted.add(k["name"])
                    break
        self._save_state()

    def reset(self):
        """Reset all keys to available (e.g., at start of new month)."""
        self.exhausted = set()
        self.current_index = 0
        self._save_state()

    def check_credits(self, token):
        """Check remaining credits for a key. Returns (used, total) or None."""
        try:
            url = f"https://api.apify.com/v2/users/me?token={token}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10, context=_SSL_CTX) as resp:
                data = json.loads(resp.read().decode()).get("data", {})
            plan = data.get("plan", {})
            total = plan.get("monthlyUsageCreditsUsd", 0)
            return {"email": data.get("email"), "total": total, "plan": plan.get("id")}
        except Exception:
            return None

    def status(self):
        """Print pool status."""
        print(f"Apify Key Pool — {len(self.keys)} keys loaded")
        total_credits = 0
        for k in self.keys:
            exhausted = "EXHAUSTED" if k["name"] in self.exhausted else "available"
            info = self.check_credits(k["token"])
            if info:
                credits = info["total"]
                total_credits += credits
                print(f"  {k['name']:25s} {info['email']:35s} ${credits:.2f}/mo  [{exhausted}]")
            else:
                print(f"  {k['name']:25s} {'?':35s} $?.??/mo  [{exhausted}]")
        print(f"\n  Total free credits: ${total_credits:.2f}/mo")
        available = len([k for k in self.keys if k["name"] not in self.exhausted])
        print(f"  Available keys: {available}/{len(self.keys)}")


if __name__ == "__main__":
    pool = ApifyKeyPool()
    pool.status()
