from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm

def coder_agent(state):
    task = state["task"]
    plan = state["plan"]

    prompt = f"""
You are an expert Python software engineer.

Task:
{task}

Implementation Plan:
{plan}

Requirements:
1. Generate only Python code.
2. Do not explain anything.
3. Do not use markdown.
4. Do not use triple backticks.
5. Do not provide examples.
6. Do not provide test cases.
7. Output must be directly executable.
8. Follow PEP8.
"""

    response = llm.invoke(prompt)

    return {
    "code": response.content,
    "current_agent": "coder"
}