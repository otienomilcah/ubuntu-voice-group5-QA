# Ubuntu Voice — Group 5 QA Automation

Independent QA automation repository for **Group 5** testing of the Ubuntu Voice Hackathon project.

The repository contains BDD-based API automation, controlled test data, automated scenarios, test reports, CI configuration, and supporting QA documentation.

Automated scenarios are mapped to the Group 5 manual QA test inventory to provide traceability from requirements through test execution and defects.

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

**Original Project Repository**

https://github.com/mainanorbert/ubuntu_voice

**Ubuntu Voice User Guide**

https://github.com/mainanorbert/ubuntu_voice/blob/main/Hackathon_QA_project_user_guide.md

**Project Demo**

https://www.youtube.com/watch?v=_O3LJtk8dBo

---

# 2. Group 5 QA Team

| Member | Role |
|---|---|
| Milka Otieno | QA Coordinator / Tester / Automation |
| Chipukizii | QA Tester / Automation Contributor |

Group 5 operates independently from the other hackathon testing groups.

---

# 3. QA Objectives

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

# 4. QA Scope

Testing covers the following areas.

## 4.1 Functional / UI

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

## 4.2 AI / Voice

- Voice/chat interaction
- Relevant responses
- Unsupported questions
- Ambiguous requests
- Multilingual input
- Unexpected language handling
- AI response consistency
- High-risk information handling

## 4.3 RAG / Knowledge Retrieval

- Knowledge grounding
- Retrieval from trusted documents
- Unsupported questions
- Cross-agent knowledge isolation
- Cross-agent document isolation
- Source/citation consistency
- Response relevance
- Response consistency

## 4.4 Emergency Reporting

- Casualties
- Severe hunger
- Displacement
- Rights violations
- Non-incident messages
- Repeated reports
- Report quantities
- Emergency classification

## 4.5 Alerts / Notifications

- Emergency alert generation
- Alert content
- Alert consistency with submitted reports

## 4.6 Statistics

- Incident creation
- Incident classification
- Category accuracy
- Quantity/count accuracy
- Agent association
- Repeated incident handling

## 4.7 Map

- Known location recognition
- Map markers
- Unknown location handling
- Location consistency
- GPS-related behavior

## 4.8 Agent Lifecycle

- Agent creation
- Required fields
- Agent purpose validation
- Document upload
- Document processing
- Agent approval
- Public agent availability
- Restrictions on unapproved agents

## 4.9 WhatsApp

- Greeting
- Agent menu
- Agent selection
- Agent switching
- Agent response
- Agent isolation

## 4.10 Evaluation

- Evaluation dataset creation
- Correctness scoring
- Groundedness scoring
- Relevance scoring
- Agent association
- Evaluation consistency

## 4.11 Security / Privacy

- Authentication
- Authorization
- Session handling
- Protected functionality
- Cross-agent data isolation
- Document isolation
- Unauthorized access
- Credential/secret exposure

## 4.12 Usability / Accessibility

- Workflow clarity
- Error-message clarity
- Keyboard navigation
- Readability
- Mobile usability
- Accessibility barriers

## 4.13 Compatibility

- Chrome
- Firefox
- Mobile browsers
- Responsive layouts

## 4.14 Regression

- Authentication
- Agent management
- RAG
- Emergency reporting
- Statistics
- Map
- Evaluation
- WhatsApp

---

# 5. Automation Approach

Group 5 uses **Behavior-Driven Development (BDD)** for API/service automation.

The automation focuses on high-value business and service workflows rather than attempting to automate every manual test case.

The automation validates areas such as:

- Authentication
- Agent management
- Agent approval
- Document processing
- RAG/knowledge retrieval
- Emergency reporting
- Emergency classification
- Emergency statistics
- Evaluation
- Regression scenarios

BDD scenarios are written in business-readable language and mapped to the corresponding manual test-case IDs.

### Example

```gherkin
@TC-070
Scenario: Agent answers using information from its uploaded document
  Given an approved agent has a trusted knowledge document
  When I ask the agent a question covered by the document
  Then the response should contain information grounded in the document
