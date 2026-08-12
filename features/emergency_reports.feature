Feature: Emergency reporting

  Scenario: Submit a valid emergency report (Severe Hunger)
    Given the cloud API is reachable and healthy
    When the user sends the prompt "Severe hunger is affecting families in Nyala; ~200 people need food assistance." to agent "Sudan Peace Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system
