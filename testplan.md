# Ubuntu Voice — Group 5 QA Test Plan

**Document ID:** QA-PLAN-001  
**Team:** Group 5  
**Project:** Ubuntu Voice Hackathon
**Application:** Ubuntu Voice  
**Environment:** Live  
**QA Team Size:** 2  
**Test Lead/Coordinator:** Milka Otieno  
**Status:** Draft  

---

## 1. Objective

This Test Plan defines how Group 5 will organize, execute, document and report testing of the Ubuntu Voice application.

The plan translates the QA Test Strategy into an actionable testing workflow covering requirements, test scenarios, execution, defects, evidence and regression.

---

## 2. Test Environment

**Application:**  
https://ubuntuvoice.agentrixx.com/

**User Guide:**  
https://github.com/mainanorbert/ubuntu_voice/blob/main/Hackathon_QA_project_user_guide.md

**Repository:**  
https://github.com/mainanorbert/ubuntu_voice

Testing will be performed primarily against the available live application unless another environment is provided.

---

## 3. Test Team and Responsibilities

| Team Member | Role | Responsibility |
|---|---|---|
| Milka Otieno | QA Coordinator / Tester | Coordinate QA activities, requirements coverage, test allocation, functional/integration testing, defect review and final QA summary |
| Chipukizii | QA Tester | Execute assigned test cases, document results, capture evidence and report defects |

Both testers may execute tests across different test areas based on the approved test inventory. Assignments will be made to minimize duplicate testing.

---

## 4. Test Areas

Testing will consider the following areas:

- Functional/UI
- Voice/AI
- RAG/Knowledge Retrieval
- API/Integration
- Security
- Performance
- Usability/Accessibility
- Compatibility
- Regression

Not every test case will require all test areas. Each test case will be assigned the most relevant Test Area.

---

## 5. Requirements and Test Inventory

The team will review the Ubuntu Voice User Guide before creating detailed test cases.

The review will identify:

- Features and user workflows
- Functional requirements
- Expected behavior
- User roles and permissions
- AI/Voice behavior
- RAG/knowledge retrieval behavior
- Integrations
- Business rules
- Preconditions and limitations

The identified requirements and scenarios will form the Group 5 QA test inventory.

Each test case will be traceable to a requirement or feature where practical.

---

## 6. Test Case Design

Test cases will be created from the approved test inventory.

Each test case should capture, where applicable:

- Test Case ID
- Requirement/Feature
- Test Scenario
- Preconditions
- Test Steps
- Expected Result
- Test Area
- Priority
- Severity
- Assigned Tester
- Environment
- Execution Result
- Evidence
- Defect Reference

---

## 7. Test Execution

For each assigned test case, the tester will:

1. Review the scenario and expected result.
2. Verify the test environment and required test data.
3. Execute the test steps.
4. Record the actual result.
5. Mark the result as Passed, Failed, Blocked or Not Run.
6. Attach relevant evidence.
7. Report a defect where the expected result is not achieved.
8. Retest resolved defects.
9. Perform regression testing for affected functionality.

---

## 8. Defect Management

Defects will be reported using GitHub Issues in the Ubuntu Voice repository, where appropriate.

A defect should include:

- Clear title
- Test Case ID
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Evidence
- Tester
- Related requirement/feature

Critical and High defects should be reviewed by the QA Coordinator before final reporting.

---

## 9. Severity

| Severity | Definition |
|---|---|
| Critical | System unavailable, severe security issue, major data loss or critical functionality failure |
| High | Major functionality unavailable or significantly incorrect |
| Medium | Important functionality affected but a workaround exists |
| Low | Minor functional, usability or cosmetic issue |

---

## 10. Test Results

| Result | Meaning |
|---|---|
| Passed | Expected result achieved |
| Failed | Expected result not achieved |
| Blocked | Test cannot be completed because of a blocking issue |
| Not Run | Test has not yet been executed |
| Not Applicable | Test does not apply to the scenario |

---

## 11. Evidence

Evidence should be captured where useful to demonstrate test execution or defects.

Examples include:

- Screenshots
- Screen recordings
- API responses
- Console/log information
- Browser/device information
- Relevant test data

Evidence should clearly support the recorded result.

---

## 12. Entry Criteria

Testing can begin when:

- The application is accessible.
- The User Guide is available.
- Requirements and key workflows have been identified.
- Test scenarios have been created.
- Test cases have been assigned.
- Required accounts or test data are available.

---

## 13. Exit Criteria

Testing will be considered complete when:

- Critical workflows have been tested.
- High-risk scenarios have been covered.
- Critical/High defects have been assessed.
- Fixed defects have been retested where applicable.
- Relevant regression testing has been completed.
- Remaining risks and limitations have been documented.
- Final QA results have been summarized.

---

## 14. Deliverables

Group 5 will maintain the following QA deliverables:

1. QA Test Strategy
2. QA Test Plan
3. Requirements/Test Inventory
4. Test Cases
5. Test Execution Results
6. Defect Reports
7. Test Evidence
8. Regression Results
9. Final QA Summary

---

## 15. Collaboration

- Milka will coordinate test allocation, coverage and overall QA reporting.
- Chipukizii and Milka will update their assigned test cases as execution progresses.
- Testers should avoid duplicate execution unless independent verification or regression is required.
- Defects should contain sufficient information for reproduction.
- Significant findings and requirement ambiguities should be discussed between the two testers.
- The final QA summary will reflect the combined results of both testers.

---

## 16. Change Control

Any significant change to application behavior, requirements or testing scope identified during testing will be documented and assessed for its impact on existing test cases and regression coverage.