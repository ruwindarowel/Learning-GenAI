import LangChainApp as lca
import streamlit as st

st.title("Pets name generator")

animal_type = st.selectbox("What is your pet?",("Dog","Cat","Hamster","Parrot"))

if animal_type=='Dog':
    pet_color = st.text_input("What color is your dog?",
                             max_chars=8)
    
if animal_type=='Cat':
    pet_color = st.text_input("What color is your cat?",
                             max_chars=8)
    
if animal_type=='Hamster':
    pet_color = st.text_input("What color is your Hamster?",
                             max_chars=8)
    
if animal_type=='Parrot':
    pet_color = st.text_input("What color is your Parrot?",
                             max_chars=8)
    
if pet_color:
    response = lca.generate_pet_name(animal_type = animal_type,
                                     pet_color = pet_color)
    names = response['text']
    st.header("Suggested Pet Names")
    st.text(names)