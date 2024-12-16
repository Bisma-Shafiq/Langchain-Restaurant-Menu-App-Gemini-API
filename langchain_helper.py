import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not found. Please set it in your .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Language Model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=GOOGLE_API_KEY)

def generate_items(cuisine):
    try:
        # Chain #1: Restaurant Name
        prompt_template_name = PromptTemplate(
            input_variables=["cuisine"],
            template="I want to open a restaurant for {cuisine} food. Suggest some fancy names for this restaurant."
        )
        name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

        # Chain #2: Menu
        prompt_template_menu = PromptTemplate(
            input_variables=["restaurant_name"],
            template="Create a menu for {restaurant_name}. Suggest 5-6 signature dishes that represent the restaurant's cuisine."
        )
        food_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu_items")

        # Sequential Chain
        chain = SequentialChain(
            chains=[name_chain, food_chain],
            input_variables=["cuisine"],
            output_variables=["restaurant_name", "menu_items"]
        )

        # Generate response
        response = chain({"cuisine": cuisine})
        return {
            "restaurant_name": response["restaurant_name"],
            "menu_items": response["menu_items"]
        }

    except Exception as e:
        raise RuntimeError(f"Error generating items: {str(e)}")
