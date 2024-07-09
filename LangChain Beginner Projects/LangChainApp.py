from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.agents import initialize_agent
from langchain.agents import load_tools
from langchain.agents import AgentType

from dotenv import load_dotenv

import warnings
warnings.filterwarnings('ignore')

load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.9)
    
    prompt_template_name = PromptTemplate(
        input_variable = ['animal_type','pet_color'],
        template = "I have a {animal_type} and it is {pet_color} in color. Suggest me 5 cool names for it."
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    
    response = name_chain({'animal_type': animal_type,
                           'pet_color': pet_color}
                          )
    return response

def langchain_agent():
    llm = OpenAI(temperature=0.5)
    
    tools = load_tools(['wikipedia','llm-math'],
                       llm=llm)
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    
    result = agent.run(
        "What is the average age of a dog? Multiply age by 3"
    )
    
    print(result)
    
langchain_agent()