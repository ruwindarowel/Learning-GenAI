import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os

with st.sidebar:
    st.title("Langchain Project")
    st.text("Made as project to learn Langchain, Streamlit and RAG")
    
    API_KEY = st.text_input("Enter API Key : ")
    
load_dotenv(
    
)
def main():
    st.header("Chat with PDF 🗨")
    
    pdf = st.file_uploader("Upload yor PDF", type='pdf')
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        
        text =""
        
        for page in pdf_reader.pages:
            text += page.extract_text()
                    
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)
        
        #embeddings
        store_name = pdf.name[:-4]
        st.write(f'{store_name}')
        if os.path.exists(f"{store_name}.pkl"):
            x = FAISS.load_local(f"{store_name}", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
            VectorStore = x.as_retriever()
                
        else:
            embeddings = OpenAIEmbeddings()        
            VectorStore = FAISS.from_texts(chunks,embedding=embeddings)
            VectorStore.save_local(f"{store_name}")
                
        query = st.text_input("Ask question about your PDF file:")
        
        if query:
            docs = VectorStore.similarity_search(query=query, k=3)
            
            llm = OpenAI()
            chain = load_qa_chain(
                llm=llm,
                chain_type='stuff'
            )
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs,
                                     question=query)
                print(cb)
            st.write(response)
                
                
        
        
    
    
if __name__ == '__main__':
    main()

    


    

