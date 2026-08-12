Feature: WhatsApp webhook flow

  Scenario: New user receives agent menu
    Given the cloud API is reachable and healthy
    When a Twilio WhatsApp webhook is sent with body "Hi" and from "+254106539556"
    Then the response status should be 200

  Scenario: User selects an agent and asks a question
    Given the cloud API is reachable and healthy
    When a Twilio WhatsApp webhook is sent with body "1" and from "+254106539556"
    Then the response status should be 200

  Scenario: User sends an emergency report via WhatsApp
    Given the cloud API is reachable and healthy
    When a Twilio WhatsApp webhook is sent with body "What is the situation in Sudan regarding displacement?" and from "+254106539556"
    Then the response status should be 200
