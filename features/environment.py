"""
Behave environment hooks for Ubuntu Voice BDD test suite.

before_all: Dynamically resolves approved agent IDs from the live
/api/v1/companies/public endpoint so the suite never breaks when
agents are recreated on the shared hackathon backend.
"""

import requests

API_BASE_URL = "https://ubuntu-voice-b.vercel.app"
PUBLIC_AGENTS_ENDPOINT = f"{API_BASE_URL}/api/v1/companies/public"

# Friendly name aliases -> partial name match against live API response.
# If a live agent name CONTAINS the alias key, it is selected.
# This handles names like "TEST - Sudan Peace Agent" matching "Sudan Peace Agent".
AGENT_ALIASES = {
    "Sudan Peace Agent":    "Sudan",
    "Somalia Agent":        "Somalia",
    "Meridia Peace Agent":  "Meridia",
    "Sudan Response Agent": "Sudan Response",
}


def before_all(context):
    """
    Runs ONCE before the entire test suite.

    Fetches all currently approved agents from the live backend and builds
    a dynamic name -> company_id map so tests never fail due to stale UUIDs.
    """
    context.agent_map = {}

    try:
        response = requests.get(PUBLIC_AGENTS_ENDPOINT, timeout=15)
        if response.status_code != 200:
            print(
                f"\n[WARN] Could not fetch agents from {PUBLIC_AGENTS_ENDPOINT}. "
                f"Status: {response.status_code}. Falling back to hardcoded IDs."
            )
            return

        live_agents = response.json()  # list of {id, name, is_approved, ...}

        for alias, keyword in AGENT_ALIASES.items():
            # Find the first live approved agent whose name contains the keyword
            match = next(
                (a for a in live_agents
                 if keyword.lower() in a.get("name", "").lower()
                 and a.get("is_approved") is True),
                None,
            )
            if match:
                context.agent_map[alias] = match["id"]
                print(
                    f"[INFO] Resolved '{alias}' -> '{match['name']}' ({match['id']})"
                )
            else:
                print(
                    f"[WARN] No approved agent found matching keyword '{keyword}'. "
                    f"Tests using '{alias}' may fail."
                )

    except requests.exceptions.RequestException as exc:
        print(
            f"\n[WARN] Could not reach backend to resolve agent IDs: {exc}. "
            f"Tests will use any IDs already set in KNOWN_AGENTS."
        )
