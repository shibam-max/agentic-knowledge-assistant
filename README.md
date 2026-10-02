# Agentic Knowledge Assistant

A production-minded AI agent project built for portfolio impact and GenAI/agentic AI job interviews. The system helps a user ask natural-language questions about internal knowledge, fetch relevant documents, reason through the best answer, and produce a concise action summary.

## Why this project matters

This project is designed to showcase:

- Retrieval-augmented generation (RAG)
- Multi-step agent reasoning
- Tool-using architecture patterns
- Local-first development with optional cloud LLM integration
- Real-world product thinking for enterprise assistant workflows

It is suitable for AI engineer, ML engineer, and GenAI product roles.

## Core idea

The assistant:

1. Understands the user's intent
2. Searches a local knowledge base
3. Extracts the most relevant source passages
4. Synthesizes an answer using a language model or deterministic fallback
5. Returns a structured response plus next steps

## Architecture

- `src/agentic_knowledge_assistant/agent.py` — orchestration logic for the AI agent
- `src/agentic_knowledge_assistant/knowledge_base.py` — document loading and retrieval
- `src/agentic_knowledge_assistant/llm.py` — optional cloud LLM integration and local fallback
- `src/agentic_knowledge_assistant/config.py` — settings and environment handling
- `data/knowledge/` — sample knowledge documents
- `streamlit_app.py` — easy interactive demo UI
- `tests/` — validation and smoke tests

## Features

- Local document retrieval with weighted ranking
- Optional OpenAI / AWS Bedrock integration via environment variables
- Structured agent workflow for question answering
- Safe fallback when an external model is unavailable
- Interactive web demo using Streamlit
- Production-style README and project documentation

## Project structure

```text
agentic-knowledge-assistant/
├── data/
│   └── knowledge/
│       ├── product_overview.md
│       ├── onboarding_guide.md
│       └── support_playbook.md
├── src/
│   └── agentic_knowledge_assistant/
│       ├── __init__.py
│       ├── agent.py
│       ├── config.py
│       ├── knowledge_base.py
│       └── llm.py
├── tests/
│   └── test_agent.py
├── .env.example
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── streamlit_app.py
└── README.md
```

## Quick start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Run the agent from the terminal

```bash
python -m src.agentic_knowledge_assistant.agent "How do we onboard a new customer?"
```

### 3. Launch the Streamlit UI

```bash
streamlit run streamlit_app.py
```

### 4. Optional cloud model configuration

Copy the sample env file:

```bash
cp .env.example .env
```

Then set one of the following:

- `OPENAI_API_KEY` for OpenAI
- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for Bedrock

The demo still works without these by using the built-in local reasoning fallback.

## Example questions

- How does the onboarding process work?
- What are the common customer support escalation steps?
- What are the product priorities for this quarter?
- What is the recommended next action for a new customer?

## Skills demonstrated

This project showcases a practical set of GenAI skills:

- Prompt engineering and instruction design
- Retrieval and grounding
- Agent memory and workflow orchestration
- Evaluation-friendly architecture
- Deployment-ready README and portfolio presentation

## Suggested interview talking points

- Explain the difference between a chatbot and an agentic workflow
- Describe how retrieval grounding reduces hallucination risk
- Show how tool selection and structured outputs support real enterprise workflows
- Discuss where LLM fallbacks and guardrails are necessary in production systems

## License

MIT
