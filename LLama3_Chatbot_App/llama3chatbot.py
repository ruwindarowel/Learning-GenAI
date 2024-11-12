from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
import streamlit as st

#Backend


prompt_chain = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful HR assistant. Your role is to Please respond accordingly."),
        ("user","Question:{question}")
    ]
)

#Creating a chain containing the prompt and llm
#Streamlit Frontend
with st.sidebar:
    st.title("Llama3 Chatbot")
    temp = st.slider("Select Temperature",min_value=0.0,max_value=1.0)
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#React to user input
prompt = st.chat_input("What is up?")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
        
    st.session_state.messages.append({"role": "user",
                                      "content":prompt})
    llm = Ollama(model="llama3",temperature=temp)
    
    chain = prompt_chain|llm
    response = chain.invoke({"question":prompt})
    
    with st.chat_message("assistant"):
        st.markdown(response)
        
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
            }
        )
    
