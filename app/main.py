import streamlit as st
from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from pathlib import Path
from router import router

#faqs_path = Path(__file__).parent / "resources/faq_data.csv"
faqs_path = Path(__file__).parent.parent / "resources" / "faq_data.csv"
ingest_faq_data(faqs_path)


def ask(query):
    route = router(query).name

    if route == 'faq':
        return faq_chain(query)

    elif route == 'sql':
        return sql_chain(query)

    else:
        return faq_chain(query)



css_path = Path(__file__).parent / "style.css"

with open(css_path, encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("E-commerce Bot")

query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role":"user", "content":query})

    response = ask(query)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


