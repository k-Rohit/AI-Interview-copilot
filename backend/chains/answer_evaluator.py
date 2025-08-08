from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv() # Load environment variables from .env file

# Initialize the OpenAI model
model = ChatOpenAI(
     model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
     temperature=0.1,
)


