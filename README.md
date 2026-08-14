# Ubuntu Voice — Group 5 QA Automation

Independent QA automation repository for **Group 5** testing of the Ubuntu Voice Hackathon project.

The repository contains BDD-based API automation, controlled test data, automated scenarios, test reports, CI configuration, and supporting QA documentation.

Automated scenarios are mapped to the Group 5 manual QA test inventory to provide traceability from requirements through test execution and defects.

---

## 📌 Master QA Sheet & Bug Submission Link

> 📊 **Master Google Sheet Submission:** [Ubuntu Voice Bug submission_5](https://docs.google.com/spreadsheets/d/1jC0bL2WU90RI1IfeQmnR1OlT7qlD3RJx_WE0xtJwfwk/edit?usp=sharing)

This master sheet contains:
1. **Bug Reports (`Buglist` tab):** Complete, reproducible bug entries (UV-1 through UV-4) following all Andela Bug Hunt Submission Standards.
2. **Functional Test Cases (`All Test Cases` tab):** The 90+ comprehensive manual & automated test case inventory covering Functional, Security, RAG, API, Usability, and WhatsApp integrations.

---

## 1. Project Under Test

### Ubuntu Voice

Ubuntu Voice is an AI/RAG-powered platform designed to help conflict-affected communities navigate emergencies and access peace and humanitarian assistance information.

The platform supports users in:

- Reporting emergencies
- Receiving emergency and peace-related information
- Interacting with specialized AI agents
- Retrieving information from trusted agent-specific knowledge sources
- Evaluating AI agent responses
- Generating emergency alerts
- Recording emergency statistics
- Visualizing incidents on a map
- Interacting with agents through WhatsApp

### System Under Test

**Live Application**
https://ubuntuvoice.agentrixx.com/

**Live Backend Cloud API**
https://ubuntu-voice-b.vercel.app

**Original Project Repository**
https://github.com/mainanorbert/ubuntu_voice

**Ubuntu Voice User Guide**
https://github.com/mainanorbert/ubuntu_voice/blob/main/Hackathon_QA_project_user_guide.md

**Project Demo**
https://www.youtube.com/watch?v=_O3LJtk8dBo

---

## 2. Group 5 QA Team

| Member | Role |
|---|---|
| Milka Otieno | QA Coordinator / Tester / Automation |
| Gilton Koech (Chipukizii) | QA Tester / Automation Contributor |

Group 5 operates independently from the other hackathon testing groups.

---

## 3. QA Objectives

The objectives of Group 5 testing are to:

1. Validate critical Ubuntu Voice user workflows.
2. Verify AI/RAG responses are grounded in the correct knowledge base.
3. Verify isolation between agents and their documents.
4. Validate emergency reporting and classification.
5. Verify emergency alerts and notifications.
6. Verify statistics and map updates.
7. Validate agent creation, document management and approval.
8. Verify WhatsApp agent interaction.
9. Validate AI agent evaluation functionality.
10. Identify functional, security, privacy, usability, accessibility and compatibility defects.
11. Automate high-value API/service scenarios using BDD.
12. Maintain traceability between manual test cases and automated scenarios.

---

## 4. QA Scope

Testing covers the following areas:

### 4.1 Functional / UI
- Application availability
- Authentication
- Primary chat workflow
- Agent selection
- Agent switching
- Agent creation
- Agent approval
- Document management
- Error handling
- Dashboard functionality

### 4.2 AI / Voice
- Voice/chat interaction
- Relevant responses
- Unsupported questions
- Ambiguous requests
- Multilingual input
- Unexpected language handling
- AI response consistency
- High-risk information handling

### 4.3 RAG / Knowledge Retrieval
- Knowledge grounding
- Retrieval from trusted documents
- Unsupported questions
- Cross-agent knowledge isolation
- Cross-agent document isolation
- Source/citation consistency
- Response relevance
- Response consistency

### 4.4 Emergency Reporting
- Casualties
- Severe hunger
- Displacement
- Rights violations
- Non-incident messages
- Repeated reports
- Report quantities
- Emergency classification

### 4.5 Alerts / Notifications
- Emergency alert generation
- Alert content
- Alert consistency with submitted reports

### 4.6 Statistics
- Incident creation
- Incident classification
- Category accuracy
- Quantity/count accuracy
- Agent association
- Repeated incident handling

### 4.7 Map
- Known location recognition
- Map markers
- Unknown location handling
- Location consistency
- GPS-related behavior

### 4.8 Agent Lifecycle
- Agent creation
- Required fields
- Agent purpose validation
- Document upload
- Document processing
- Agent approval
- Public agent availability
- Restrictions on unapproved agents

### 4.9 WhatsApp
- Greeting
- Agent menu
- Agent selection
- Agent switching
- Agent response
- Agent isolation

### 4.10 Evaluation
- Evaluation dataset creation
- Correctness scoring
- Groundedness scoring
- Relevance scoring
- Agent association
- Evaluation consistency

### 4.11 Security / Privacy
- Authentication
- Authorization
- Session handling
- Protected functionality
- Cross-agent data isolation
- Document isolation
- Unauthorized access
- Credential/secret exposure

### 4.12 Usability / Accessibility
- Workflow clarity
- Error-message clarity
- Keyboard navigation
- Readability
- Mobile usability
- Accessibility barriers

### 4.13 Compatibility
- Chrome
- Firefox
- Mobile browsers
- Responsive layouts

### 4.14 Regression
- Authentication
- Agent management
- RAG
- Emergency reporting
- Statistics
- Map
- Evaluation
- WhatsApp

---

## 5. Automation Approach & Execution Guide

Group 5 uses **Behavior-Driven Development (BDD)** for API/service automation via **Python**, **Behave**, and **Requests**.

The automation suite executes **17 automated end-to-end scenarios** across 4 feature files targeting the live cloud API.

### 5.1 How to Install and Run Automated Tests

```powershell
# 1. Clone the repository
git clone https://github.com/otienomilcah/ubuntu-voice-group5-QA.git
cd ubuntu-voice-group5-QA

# 2. Set up virtual environment
python -m venv venv
.\venv\Scripts\activate      # On Windows
# source venv/bin/activate   # On Linux/macOS

# 3. Install dependencies
pip install behave requests

# 4. Run the BDD automation suite
behave --no-capture
```

### 5.2 Evidence of Passing Execution Log

Below is the verified terminal log from the latest test run:

```text
Feature: Test Live Cloud AI Agent # features/agent_chat.feature:1
  Scenario: Health check passes on the live backend                             # PASSED
  Scenario: Send a general greeting to an approved agent                       # PASSED
  Scenario: Agent answers an in-scope question about Sudan                     # PASSED
  Scenario: Agent politely refuses an out-of-scope question                   # PASSED
  Scenario: Unapproved or nonexistent agent returns 404                       # PASSED
  Scenario: Empty message is rejected with 422 Unprocessable Entity            # PASSED
  Scenario: Oversized message is rejected with 422 Unprocessable Entity        # PASSED
  Scenario: Chat with history context works correctly                          # PASSED
  Scenario: Somalia agent responds to queries                                  # PASSED

Feature: Authentication and Security # features/auth_security.feature:1
  Scenario: Unauthenticated user cannot create an agent                        # PASSED (Returns 401)
  Scenario: Unauthenticated user cannot access guardrail audit events          # PASSED (Returns 401)
  Scenario: Unauthenticated user cannot access known places endpoint           # PASSED (Returns 401)
  Scenario: Incident statistics rejects unauthenticated access (invalid params)# PASSED (Returns 401)

Feature: Emergency reporting # features/emergency_reports.feature:1
  Scenario: Submit a valid emergency report (Severe Hunger)                    # PASSED

Feature: WhatsApp webhook flow # features/whatsapp.feature:1
  Scenario: New user receives agent menu                                       # PASSED (HTTP 200 ACK)
  Scenario: User selects an agent and asks a question                          # PASSED (HTTP 200 ACK)
  Scenario: User sends an emergency report via WhatsApp                        # PASSED (HTTP 200 ACK)

--------------------------------------------------------------------------------
4 features passed, 0 failed, 0 skipped
17 scenarios passed, 0 failed, 0 skipped
62 steps passed, 0 failed, 0 skipped
Took 1min 33.075s
```

---

## 6. Discovered Bugs (Submission Standard Checklist)

All defects discovered during testing follow the **Andela Bug Hunt Submission Checklist**:

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
  - *Expected:* The dashboard greeting should correspond to the current time of day.
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
*Maintained by Group 5 (Milka Otieno & Gilton Koech) for the Ubuntu Voice QA Hackathon Challenge.*
