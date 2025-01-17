from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("API_KEY")

llm = ChatGroq(groq_api_key = api_key, model_name="llama-3.3-70b-versatile")
