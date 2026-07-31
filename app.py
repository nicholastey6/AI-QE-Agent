import streamlit as st

from agent import ask_agent


st.title(
"AI Quality Engineering Assistant"
)


question = st.text_input(
"Describe your failure:"
)


if question:

    answer = ask_agent(question)

    st.write(answer)
