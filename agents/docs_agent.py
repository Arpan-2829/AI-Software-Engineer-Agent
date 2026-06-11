from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm


def docs_agent(state):
    task = state["task"]
    code = state.get(
    "fixed_code",
    state["code"])

    prompt = f"""
You are a senior software engineer.

Task:

{task}

Code:

{code}

Write:

1. Function explanation
2. Inputs
3. Outputs
4. Time complexity
5. Space complexity

Do not generate code.
"""

    response = llm.invoke(prompt)

    return {
        "documentation": response.content
    }