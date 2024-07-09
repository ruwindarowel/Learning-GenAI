import streamlit as st
import langchain_agent as la
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Enter the YouTube URL",
            max_chars=50
        )
        
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )
        
        submit_button = st.form_submit_button(label="Summarize")
        
if query and youtube_url:
    db = la.create_vector_db_from_youtube_url(youtube_url)
    response, docs = la.get_response_from_query(db=db, query=query)
    st.subheader("Answer")
    st.text(textwrap.fill(response, width=100))