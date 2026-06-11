from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm


def tester_agent(state):
    code = state.get(
        "fixed_code",
        state["code"])

    prompt = f"""
You are a pytest expert.

Generate unit tests for the following code.

Return only pytest code.

Code:

{code}
"""

    response = llm.invoke(prompt)

    return {
        "tests": response.content
    }