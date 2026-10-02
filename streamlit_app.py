from __future__ import annotations

import streamlit as st

from src.agentic_knowledge_assistant.agent import run_agent

st.set_page_config(page_title="Agentic Knowledge Assistant", page_icon="🤖")
st.title("Agentic Knowledge Assistant")
st.caption("A portfolio-ready GenAI agent for grounded question answering and action planning.")

question = st.text_input(
    "Ask a question about your knowledge base",
    value="How do we onboard a new customer?",
)

if st.button("Run agent"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving context and synthesizing an answer..."):
            result = run_agent(question)

        st.subheader("Answer")
        st.write(result["answer"])

        st.subheader("Source documents")
        for source in result["sources"]:
            st.markdown(f"- **{source['title']}**: {source['snippet']}")
