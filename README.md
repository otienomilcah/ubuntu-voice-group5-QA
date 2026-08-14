# 🚀 Ubuntu Voice — Group 5 QA Backend Test Automation Suite

![BDD Tests](https://img.shields.io/badge/BDD-14%20Scenarios-blue)
![Latest Run](https://img.shields.io/badge/Latest%20Run-14%20Passed-brightgreen)
![Framework](https://img.shields.io/badge/Framework-Python%20%7C%20Behave%20%7C%20Requests-blue)
![Target](https://img.shields.io/badge/Target-Live%20Cloud%20API-orange)

> **Document ID:** QA-EXEC-001  
> **Project:** Ubuntu Voice Hackathon Challenge  
> **Team:** Group 5  
> **QA Team:** Milka Otieno (QA Coordinator / Tester) & Gilton Koech / Chipukizii (QA Tester)  
> **Automation Type:** BDD API Automation  
> **Current Automated Scenarios:** 14  
> **Latest Execution:** 14 Passed / 0 Failed

---

# 1. Executive Summary

This repository contains Group 5's independent QA automation suite for the **Ubuntu Voice** platform.

Ubuntu Voice is an AI/RAG-powered platform designed to help conflict-affected communities access peace and humanitarian information and report emergencies.

The automation suite uses:

- **Python 3**
- **Behave (BDD)**
- **Requests**
- Live cloud API endpoints

The current automation suite contains **14 BDD scenarios**, all of which passed in the latest execution.

The automated coverage focuses on high-value backend/API behavior including:

- API health
- AI agent chat
- RAG knowledge retrieval
- Knowledge grounding
- Out-of-scope question handling
- Agent routing
- Chat history/context
- Multi-agent isolation
- Input validation
- Authentication/security
- Emergency reporting
- WhatsApp/Twilio integration

The automation is part of a broader Group 5 QA effort that also includes a **90-test-case manual QA inventory**, exploratory testing, defect discovery and regression testing.

---

# 2. System Under Test

## 2.1 Application Under Test

Ubuntu Voice live application:

https://ubuntuvoice.agentrixx.com/

The web application provides functionality including:

- User registration and authentication
- Emergency reporting
- AI agent interaction
- Agent creation
- Agent approval
- Knowledge/document upload
- RAG-based information retrieval
- Emergency alerts
- Statistics
- Map visualization
- WhatsApp interaction
- Agent evaluation

---

## 2.2 Backend API Under Test

The automated API suite currently targets:

```text
https://ubuntu-voice-b.vercel.app
