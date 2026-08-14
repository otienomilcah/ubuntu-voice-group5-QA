# 🚀 Ubuntu Voice — Group 5 QA Backend Test Automation Suite & QA Documentation

![BDD Tests](https://img.shields.io/badge/BDD-14%20Scenarios-blue)
![Latest Run](https://img.shields.io/badge/Latest%20Run-14%20Passed-brightgreen)
![Framework](https://img.shields.io/badge/Framework-Python%20%7C%20Behave%20%7C%20Requests-blue)
![Target](https://img.shields.io/badge/Target-Live%20Cloud%20API-orange)

> **Document ID:** QA-EXEC-001  
> **Project:** Ubuntu Voice Hackathon Challenge  
> **Team:** Group 5  
> **QA Team:** Milka Otieno (QA Coordinator / Tester) & Gilton Koech / Chipukizii (QA Tester)  
> **Automation Type:** BDD API Automation  
> **Current Automated Scenarios:** 14 Passed / 0 Failed  
> **Manual Test Inventory:** 90+ Test Cases  

---

# 1. Executive Summary

This repository contains Group 5's independent QA automation suite and testing deliverables for the **Ubuntu Voice** platform.

Ubuntu Voice is an AI/RAG-powered platform designed to help conflict-affected communities access peace and humanitarian information and report emergencies.

The automation suite uses:
- **Python 3**
- **Behave (BDD)**
- **Requests**
- Live cloud API endpoints (`https://ubuntu-voice-b.vercel.app`)

The automation suite contains **14 BDD scenarios**, all of which passed in the latest execution.

---

# 2. Master QA Sheet & Bug Submission Link

> 📌 **Master Google Sheet Submission:** [Ubuntu Voice Bug submission_5](https://docs.google.com/spreadsheets/d/1e06LEW098N1fcQmhRT111q-qib3rox_1H20xbWmlq_edit)

This master sheet contains:
1. **Bug Reports Tab (`Buglist`):** Complete, reproducible bug entries (UV-1 through UV-4) following all Andela Bug Hunt Submission Standards.
2. **Functional Test Cases Tab (`All Test Cases`):** The 90+ comprehensive manual & automated test case inventory covering Functional, Security, RAG, API, Usability, and WhatsApp integrations.

---

# 3. How to Install and Run the Automated BDD Tests

### Prerequisites
- Python 3.10+
- Internet connection (tests run against the live cloud backend)

### Step-by-Step Installation & Execution

```powershell
# 1. Clone the repository
git clone https://github.com/otienomilcah/ubuntu-voice-group5-QA.git
cd ubuntu-voice-group5-QA

# 2. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate      # On Windows
# source venv/bin/activate   # On Linux/macOS

# 3. Install required dependencies
pip install behave requests

# 4. Run the full BDD test suite
behave --no-capture
```

---

# 4. Evidence of Passing Test Execution

Below is the verified terminal output from the latest test run against the live cloud backend:

```text
Feature: Test Live Cloud AI Agent # features/agent_chat.feature:1
  Scenario: Health check passes on the live backend                             # PASSED
  Scenario: Send a general greeting to an approved agent                       # PASSED
  Scenario: Agent answers an in-scope question about Sudan                     # PASSED
  Scenario: Agent politely refuses an out-of-scope question                   # PASSED
  Scenario: Unapproved or nonexistent agent returns 404                     # PASSED
  Scenario: Empty message is rejected with 422 Unprocessable Entity            # PASSED
  Scenario: Oversized message is rejected with 422 Unprocessable Entity       # PASSED
  Scenario: Chat with history context works correctly                         # PASSED
  Scenario: Somalia agent responds to queries                                 # PASSED

Feature: Authentication and Security # features/auth_security.feature:1
  Scenario: Unauthenticated user cannot create an agent                       # PASSED (Returns 401)

Feature: Emergency reporting # features/emergency_reports.feature:1
  Scenario: Submit a valid emergency report (Severe Hunger)                    # PASSED

Feature: WhatsApp webhook flow # features/whatsapp.feature:1
  Scenario: New user receives agent menu                                       # PASSED (HTTP 200 ACK)
  Scenario: User selects an agent and asks a question                          # PASSED (HTTP 200 ACK)
  Scenario: User sends an emergency report via WhatsApp                        # PASSED (HTTP 200 ACK)

--------------------------------------------------------------------------------
4 features passed, 0 failed, 0 skipped
14 scenarios passed, 0 failed, 0 skipped
53 steps passed, 0 failed, 0 skipped
Took 1min 11.133s
```

---

# 5. Discovered Bugs (Submission Standard Checklist)

All defects discovered during testing strictly follow the **Andela Bug Hunt Submission Checklist**:

### 🐛 Bug UV-1: Dashboard Greeting Time Mismatch
- **Title:** Dashboard always displays "Good afternoon" regardless of current time
- **Bug ID:** UV-1
- **Environment:** Windows desktop; Google Chrome; English; Ubuntu Voice dashboard; All agents
- **Steps to reproduce:**
  1. Log in to Ubuntu Voice.
  2. Navigate to Dashboard.
  3. Observe the greeting displayed below the user's name.
  4. Access the dashboard at a different time of day and compare the greeting.
  5. Record whether the greeting changes according to the current time.
- **Expected vs Actual:**
  - *Expected:* The dashboard greeting should correspond to the current time of day (morning/afternoon/evening).
  - *Actual:* The dashboard displays "Good afternoon" regardless of the current time.
- **Frequency:** Every time observed across different times of day.
- **Severity:** Low (Cosmetic/usability).
- **Evidence:** User screenshot of dashboard at 9:00 AM displaying "Good afternoon".
- **AI Assistance Used:** N/A
- **Privacy Confirmation:** Confirmed clean; no real personal data.

### 🐛 Bug UV-2: Session Timeout Failure
- **Title:** Authenticated session remains active after prolonged inactivity, page refresh, and laptop sleep/off period
- **Bug ID:** UV-2
- **Environment:** Windows desktop; Google Chrome; Ubuntu Voice; authenticated user session; English
- **Steps to reproduce:**
  1. Log in to Ubuntu Voice using a valid account.
  2. Navigate to the Dashboard.
  3. Leave the application inactive for several hours without logging out.
  4. Return to the application and verify that the session remains authenticated.
  5. Refresh the browser tab and verify session status.
  6. Leave laptop off/asleep and return later.
  7. Reopen browser tab and navigate to authenticated routes without logging in.
- **Expected vs Actual:**
  - *Expected:* Authenticated session should be invalidated after the applicable security/session-expiration period.
  - *Actual:* Session remains authenticated after hours of inactivity and device sleep.
- **Frequency:** Consistently observed across prolonged inactivity and device sleep.
- **Severity:** High (Security risk).
- **Evidence:** Session persistence video and network logs.
- **AI Assistance Used:** N/A
- **Privacy Confirmation:** Confirmed clean; test account used.

### 🐛 Bug UV-3: API Input Validation Status Code Mismatch
- **Title:** API input validation returns HTTP 422 Unprocessable Entity instead of HTTP 400 Bad Request
- **Bug ID:** UV-3
- **Environment:** Windows desktop; Python Behave / Postman; Ubuntu Voice Cloud API (`https://ubuntu-voice-b.vercel.app`); English
- **Steps to reproduce:**
  1. Send a POST request to `https://ubuntu-voice-b.vercel.app/api/v1/agents/chat` with an empty message string (`""`).
  2. Observe the HTTP response status code and body.
  3. Send a POST request to the same endpoint with a 2100-character message string.
  4. Observe the HTTP response status code and body.
- **Expected vs Actual:**
  - *Expected:* The API should reject invalid request payloads with HTTP 400 Bad Request.
  - *Actual:* The API returns HTTP 422 Unprocessable Entity with a Pydantic validation error payload (`string_too_short` / `prompt_too_long`).
- **Frequency:** Consistently observed across 100% of empty or oversized payload tests.
- **Severity:** Medium (API specification mismatch).
- **Evidence:** Automated test logs (TC-SEC-001 & TC-SEC-002) returning 422 instead of 400.
- **AI Assistance Used:** N/A
- **Privacy Confirmation:** Confirmed clean; synthetic test strings only.

### 🐛 Bug UV-4: Next.js Frontend Proxy Returns HTML 404 for API Routes
- **Title:** Next.js frontend domain returns HTML 404 page instead of JSON error for direct API requests
- **Bug ID:** UV-4
- **Environment:** Windows desktop; Google Chrome / Postman; Ubuntu Voice frontend (`https://ubuntuvoice.agentrixx.com`); English
- **Steps to reproduce:**
  1. Send a POST request to `https://ubuntuvoice.agentrixx.com/api/v1/agents/chat` with a valid JSON body.
  2. Inspect the HTTP response `Content-Type` header and body.
  3. Send the same request directly to `https://ubuntu-voice-b.vercel.app/api/v1/agents/chat`.
  4. Compare the response content types.
- **Expected vs Actual:**
  - *Expected:* Both domains should return structured JSON responses for API routes.
  - *Actual:* Frontend domain returns a raw HTML 404 page (`Content-Type: text/html`), causing JSON parsers in API clients to crash. Backend domain correctly returns JSON.
- **Frequency:** Consistently observed on every API request sent to the frontend domain.
- **Severity:** Medium (Integration boundary issue).
- **Evidence:** API response headers showing `Content-Type: text/html` vs `application/json`.
- **AI Assistance Used:** N/A
- **Privacy Confirmation:** Confirmed clean; synthetic requests only.

---

# 6. System Under Test Reference

### Application Frontend
- URL: `https://ubuntuvoice.agentrixx.com/`

### Backend Cloud API
- URL: `https://ubuntu-voice-b.vercel.app`

---
*Maintained by Group 5 (Milka Otieno & Gilton Koech) for the Ubuntu Voice QA Hackathon Challenge.*
