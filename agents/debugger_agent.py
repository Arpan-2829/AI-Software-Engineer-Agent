from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm



def debugger_agent(state):
    code = state["code"]

    prompt = f"""
You are an expert Python debugger.

Review the following code.

Fix bugs and improve code quality.

Return only executable Python code.

Code:

{code}
"""

    response = llm.invoke(prompt)

    return {
        "fixed_code": response.content
    }