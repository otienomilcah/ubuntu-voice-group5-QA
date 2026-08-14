Feature: Authentication and Security

  Scenario: Unauthenticated user cannot create an agent
    Given the cloud API is reachable and healthy
    When I attempt to create an agent without a valid session
    Then the response status should be 401

  Scenario: Unauthenticated user cannot access guardrail audit events
    Given the cloud API is reachable and healthy
    When I attempt to access the guardrail audit events without a session
    Then the response status should be 401

  Scenario: Unauthenticated user cannot access known places monitoring endpoint
    Given the cloud API is reachable and healthy
    When I attempt to access the known places endpoint without a session
    Then the response status should be 401

  Scenario: Incident statistics endpoint rejects unauthenticated access even with invalid params
    Given the cloud API is reachable and healthy
    When I request incident statistics with an invalid page size of 999
    Then the response status should be 401
