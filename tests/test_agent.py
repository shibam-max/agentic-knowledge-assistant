from src.agentic_knowledge_assistant.agent import run_agent


def test_run_agent_returns_answer_and_sources():
    result = run_agent("How do we onboard a new customer?")

    assert isinstance(result, dict)
    assert "question" in result
    assert "answer" in result
    assert "sources" in result
    assert result["question"] == "How do we onboard a new customer?"
    assert len(result["sources"]) > 0
    assert isinstance(result["answer"], str)
    assert len(result["answer"]) > 50
