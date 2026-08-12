Feature: Authentication and Security

  Scenario: Unauthenticated user cannot create an agent
    Given the cloud API is reachable and healthy
    When I attempt to create an agent without a valid session
    Then the response status should be 401
