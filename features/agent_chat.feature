Feature: Test Live Cloud AI Agent
  As a tester
  I want to verify that the cloud AI responds to queries
  So that I know the deployment is working correctly

  Background:
    Given the cloud API is reachable and healthy

  Scenario: Health check passes on the live backend
    When I check the health endpoint
    Then the response status should be 200
    And the health status should be "ok"

  Scenario: Send a general greeting to an approved agent
    When the user sends the prompt "Hello, what can you help me with?" to agent "Sudan Peace Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system

  Scenario: Agent answers an in-scope question about Sudan
    When the user sends the prompt "What is the situation in Sudan regarding displacement?" to agent "Sudan Peace Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system
    And the response should be grounded in knowledge base documents

  Scenario: Agent politely refuses an out-of-scope question
    When the user sends the prompt "What is the price of Bitcoin?" to agent "Sudan Peace Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system
    And the response should not be grounded in knowledge base documents

  Scenario: Unapproved or nonexistent agent returns 404
    When the user sends the prompt "Hello" to agent id "00000000-0000-0000-0000-000000000000"
    Then the cloud response status should be 404

  Scenario: Empty message is rejected with 422 Unprocessable Entity
    # FastAPI returns 422 for Pydantic schema validation failures (e.g. min_length=1 violated)
    When the user sends an empty message to agent "Sudan Peace Agent"
    Then the cloud response status should be 422
    And the error detail should mention "string_too_short"

  Scenario: Oversized message is rejected with 422 Unprocessable Entity
    # FastAPI returns 422 for Pydantic schema validation failures (e.g. max_length=2000 violated)
    When the user sends a message with 2100 characters to agent "Sudan Peace Agent"
    Then the cloud response status should be 422
    And the error detail should mention "prompt_too_long"

  Scenario: Chat with history context works correctly
    When the user sends "Tell me more" with prior history "What is happening in Sudan?" to agent "Sudan Peace Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system

  Scenario: Somalia agent responds to queries
    When the user sends the prompt "Tell me about Somalia" to agent "Somalia Agent"
    Then the cloud response status should be 200
    And the response should contain an answer from the system