import streamlit as st
from langchain.llms import Ollama
from langchain_core.prompts import PromptTemplate

st.set_page_config(page_title="🧠 Prompt Evaluator (Ollama)", layout="centered")
st.title("🧠 Prompt Evaluator (Local)")

prompt_input = st.text_area("Enter your prompt", height=150)
model = st.selectbox("Choose local model", ["mistral", "phi3", "llama3"])

if st.button("Evaluate Prompt"):
    if not prompt_input.strip():
        st.warning("Prompt cannot be empty.")
    else:
        with st.spinner("Generating response..."):
            try:
                llm = Ollama(model=model)
                response = llm.invoke(prompt_input)
                st.success("Response:")
                st.code(response, language='markdown')
            except Exception as e:
                st.error(f"Error: {str(e)}")
