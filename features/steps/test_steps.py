"""
Step definitions for Ubuntu Voice cloud AI BDD tests.

API Base: https://ubuntu-voice-b.vercel.app
Endpoint: POST /api/v1/agents/chat
Required fields: company_id (str), message (str)
Optional fields: language (str, default "English"), history (list)
"""

from behave import given, when, then
import requests

# ─── Configuration ────────────────────────────────────────────────────────────
API_BASE_URL = "https://ubuntu-voice-b.vercel.app"
CHAT_ENDPOINT = f"{API_BASE_URL}/api/v1/agents/chat"
HEALTH_ENDPOINT = f"{API_BASE_URL}/health"
PUBLIC_AGENTS_ENDPOINT = f"{API_BASE_URL}/api/v1/companies/public"

# Real approved agent IDs fetched from /api/v1/companies/public
# Last refreshed: 2026-08-13 — IDs change when agents are recreated on the platform
KNOWN_AGENTS = {
    "Sudan Peace Agent":  "665e4f44-238a-4c5c-b5b7-37f7da77752f",  # TEST - Sudan Peace Agent
    "Somalia Agent":      "ca1988a1-bc92-48ea-9b37-cb478fa2bd49",  # TEST - G10 Somalia (Kirwa/Onchari)
    "Meridia Peace Agent": "f6486f7b-4fe5-451d-9fce-c4b13b9d2475", # Meridia Peace Agent (unchanged)
    "Sudan Response Agent": "906e1f9c-a815-43d2-9a1d-54db08196406", # Sudan Response Agent
}


def get_agent_id(agent_name: str) -> str:
    """
    Return the company_id for a named agent.
    Priority:
      1. context.agent_map built dynamically by before_all (environment.py)
      2. KNOWN_AGENTS hardcoded fallback
    Raises a clear ValueError if neither source has the agent.
    """
    # Access context via behave's module-level context when called from steps
    # The context object is passed per-step; use _dynamic_map as a module cache
    if agent_name in _dynamic_map:
        return _dynamic_map[agent_name]
    if agent_name in KNOWN_AGENTS:
        return KNOWN_AGENTS[agent_name]
    raise ValueError(
        f"Unknown agent '{agent_name}'. "
        f"Available in KNOWN_AGENTS: {list(KNOWN_AGENTS.keys())}. "
        f"Available in dynamic map: {list(_dynamic_map.keys())}"
    )


# Module-level cache updated by before_all via the step hook below
_dynamic_map: dict = {}


# ─── Given Steps ──────────────────────────────────────────────────────────────

@given("the cloud API is reachable and healthy")
def step_check_reachable(context):
    """Verify the backend is up and sync the dynamic agent map from before_all."""
    # Sync the dynamic map populated by environment.py before_all
    global _dynamic_map
    if hasattr(context, "agent_map") and context.agent_map:
        _dynamic_map = context.agent_map

    try:
        r = requests.get(HEALTH_ENDPOINT, timeout=10)
        assert r.status_code == 200, (
            f"Backend health check failed: {r.status_code} - {r.text}"
        )
        context.api_available = True
    except requests.exceptions.RequestException as exc:
        raise AssertionError(
            f"Could not reach backend at {API_BASE_URL}. "
            f"Error: {exc}"
        )


# ─── When Steps ───────────────────────────────────────────────────────────────

@when('I check the health endpoint')
def step_check_health(context):
    context.response = requests.get(HEALTH_ENDPOINT, timeout=10)


@when('the user sends the prompt "{prompt_text}" to agent "{agent_name}"')
def step_send_prompt_by_name(context, prompt_text, agent_name):
    company_id = get_agent_id(agent_name)
    context.response = requests.post(
        CHAT_ENDPOINT,
        json={
            "company_id": company_id,
            "message": prompt_text,
            "language": "English",
            "history": [],
        },
        timeout=30,
    )


@when('the user sends the prompt "{prompt_text}" to agent id "{company_id}"')
def step_send_prompt_by_id(context, prompt_text, company_id):
    context.response = requests.post(
        CHAT_ENDPOINT,
        json={
            "company_id": company_id,
            "message": prompt_text,
            "language": "English",
            "history": [],
        },
        timeout=30,
    )


@when('the user sends an empty message to agent "{agent_name}"')
def step_send_empty_message(context, agent_name):
    company_id = get_agent_id(agent_name)
    context.response = requests.post(
        CHAT_ENDPOINT,
        json={
            "company_id": company_id,
            "message": "",
            "language": "English",
        },
        timeout=15,
    )


@when('the user sends a message with {char_count:d} characters to agent "{agent_name}"')
def step_send_oversized_message(context, char_count, agent_name):
    company_id = get_agent_id(agent_name)
    oversized = "A" * char_count
    context.response = requests.post(
        CHAT_ENDPOINT,
        json={
            "company_id": company_id,
            "message": oversized,
            "language": "English",
        },
        timeout=15,
    )


@when('the user sends "{follow_up}" with prior history "{prior_message}" to agent "{agent_name}"')
def step_send_with_history(context, follow_up, prior_message, agent_name):
    company_id = get_agent_id(agent_name)
    context.response = requests.post(
        CHAT_ENDPOINT,
        json={
            "company_id": company_id,
            "message": follow_up,
            "language": "English",
            "history": [
                {"role": "user",      "content": prior_message},
                {"role": "assistant", "content": "Here is some context about Sudan..."},
            ],
        },
        timeout=30,
    )

@when('I attempt to create an agent without a valid session')
def step_attempt_create_agent_no_auth(context):
    context.response = requests.post(
        f"{API_BASE_URL}/api/v1/companies",
        json={
            "name": "Test Peace Agent",
            "email": "agent@test.org",
            "description": "Demo agent for testing"
        },
        timeout=15,
    )


@when('a Twilio WhatsApp webhook is sent with body "{body}" and from "{from_number}"')
def step_send_whatsapp_webhook(context, body, from_number):
    context.response = requests.post(
        f"{API_BASE_URL}/api/v1/webhooks/whatsapp/twilio",
        data={
            "From": from_number,
            "Body": body,
            "To": "+254106539556",
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        timeout=30,
    )


# ─── Then Steps ───────────────────────────────────────────────────────────────

@then("the response status should be {status_code:d}")
def step_check_response_status(context, status_code):
    assert context.response is not None, "No response was received."
    assert context.response.status_code == status_code, (
        f"Expected HTTP {status_code}, got {context.response.status_code}.\n"
        f"Response body: {context.response.text[:500]}"
    )


@then("the cloud response status should be {status_code:d}")
def step_check_cloud_response_status(context, status_code):
    assert context.response is not None, "No response was received."
    assert context.response.status_code == status_code, (
        f"Expected HTTP {status_code}, got {context.response.status_code}.\n"
        f"Response body: {context.response.text[:500]}"
    )


@then('the health status should be "{expected_status}"')
def step_check_health_status(context, expected_status):
    data = context.response.json()
    actual = data.get("status", "")
    assert actual == expected_status, (
        f"Expected health status '{expected_status}', got '{actual}'.\n"
        f"Full response: {data}"
    )


@then("the response should contain an answer from the system")
def step_check_has_reply(context):
    assert context.response is not None, "No response received."
    try:
        data = context.response.json()
    except Exception:
        raise AssertionError(
            f"Response is not valid JSON: {context.response.text[:300]}"
        )
    assert "reply" in data, f"'reply' field missing from response: {data}"
    assert len(data["reply"].strip()) > 0, "Reply field is empty."


@then("the response should be grounded in knowledge base documents")
def step_check_grounded_true(context):
    data = context.response.json()
    assert data.get("grounded") is True, (
        f"Expected grounded=True but got grounded={data.get('grounded')}.\n"
        f"Reply: {data.get('reply', '')[:300]}"
    )


@then('the response should not be grounded in knowledge base documents')
def step_check_grounded_false(context):
    data = context.response.json()
    assert data.get("grounded") is False, (
        f"Expected grounded=False (out-of-scope refusal) but got grounded={data.get('grounded')}.\n"
        f"Reply: {data.get('reply', '')[:300]}"
    )


@then('the error detail should mention "{error_type}"')
def step_check_validation_error_detail(context, error_type):
    """Assert the FastAPI 422 response body contains the expected validation error type."""
    try:
        data = context.response.json()
    except Exception:
        raise AssertionError(
            f"Expected JSON error body but got: {context.response.text[:300]}"
        )
    # FastAPI 422 bodies: {"detail": [{"type": "...", "msg": "...", ...}]}
    detail = data.get("detail", [])
    if isinstance(detail, list):
        types_found = [item.get("type", "") for item in detail]
        msgs_found  = [item.get("msg",  "") for item in detail]
        matched = any(
            error_type in t or error_type in m
            for t, m in zip(types_found, msgs_found)
        )
    elif isinstance(detail, str):
        matched = error_type in detail
    else:
        matched = False

    assert matched, (
        f"Expected error detail to mention '{error_type}'.\n"
        f"Actual detail: {detail}"
    )


@then('the response should mention unauthorized')
def step_check_unauthorized(context):
    assert context.response.status_code in [401, 403], f"Expected 401/403, got {context.response.status_code}"
    try:
        data = context.response.json()
        assert "detail" in data, "Expected detail key in error response"
    except Exception:
        assert "unauthorized" in context.response.text.lower() or "error" in context.response.text.lower()


@then('the response body should contain a numbered list of approved agents')
def step_check_whatsapp_menu(context):
    text = context.response.text
    assert "1." in text or "Reply with the number" in text, (
        f"Expected agent menu, got: {text[:300]}"
    )


@then('the response body should mention "chatting with"')
def step_check_whatsapp_chatting(context):
    text = context.response.text
    assert "chatting with" in text.lower(), (
        f"Expected confirmation of agent selection, got: {text[:300]}"
    )


@then('the response body should contain a valid answer')
def step_check_whatsapp_answer(context):
    text = context.response.text
    assert len(text.strip()) > 0, "Expected a non-empty WhatsApp reply."
    assert "Sorry, I'm having trouble" not in text, "Got fallback error reply."