#!/usr/bin/env python3
"""
Pulls live Vouch production metrics and prints a Markdown snapshot
suitable for pasting into the Demo Day deck.

Usage:
    python3 metrics_snapshot.py            # print to stdout
    python3 metrics_snapshot.py > snap.md  # save to file

No dependencies — stdlib only. Hits the public API endpoints.
"""
import json
import sys
import urllib.request
from datetime import datetime, timezone

API_BASE = "https://vouch-api-5pa4.onrender.com"
ENDPOINTS = {
    "metrics":    f"{API_BASE}/api/metrics",      # composite: signups, active_users, page_views, ratings
    "user_count": f"{API_BASE}/api/user-count",   # legacy single-field cross-check
}


def fetch(url: str, timeout: float = 60.0) -> dict:
    """GET a URL and return parsed JSON. Render free-tier cold starts can take 30-60s."""
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    try:
        m = fetch(ENDPOINTS["metrics"])
        uc = fetch(ENDPOINTS["user_count"])
    except Exception as e:
        print(f"ERROR fetching live metrics: {e}", file=sys.stderr)
        return 1

    signups       = m.get("signups", 0)
    active_users  = m.get("active_users", 0)
    page_views    = m.get("page_views", 0)
    ratings       = m.get("ratings", 0)
    user_count_xc = uc.get("user_count", 0)

    # Derived metrics — useful for the traction slide
    rpu       = round(ratings / active_users, 2) if active_users else 0.0
    actv_rate = round(100 * active_users / signups, 1) if signups else 0.0

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    print(f"# Vouch Production Metrics — {ts}\n")
    print(f"**Source:** {API_BASE}/api/metrics (live)\n")

    print("| Metric | Value |")
    print("|---|--:|")
    print(f"| Total signups | {signups} |")
    print(f"| Active users | {active_users} |")
    print(f"| Activation rate | {actv_rate}% |")
    print(f"| Total ratings logged | {ratings} |")
    print(f"| Ratings per active user | {rpu} |")
    print(f"| Total page views | {page_views} |")

    if user_count_xc != signups:
        print(f"\n> Note: `/api/user-count` returns {user_count_xc} (vs `/api/metrics.signups` = {signups}). "
              f"Endpoints may be cached differently — use `/api/metrics` as source of truth.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
