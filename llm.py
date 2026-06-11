from dotenv import load_dotenv
from langchain_groq import ChatGroq

import langsmith_config

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)