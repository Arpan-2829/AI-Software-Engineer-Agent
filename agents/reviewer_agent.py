from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm

def reviewer_agent(state):

    code = state["code"]
    error = state["execution_error"]

    prompt = f"""
You are a senior Python code reviewer.

Review the following code and execution result.

Code:
{code}

Execution Error:
{error}

Rules:
- If there is any runtime error, syntax error, exception, or major code issue, answer ONLY "YES".
- If the code is correct and executable, answer ONLY "NO".

Do not explain.
Return either YES or NO only.
"""

    response = llm.invoke(prompt)

    answer = response.content.strip().upper()

    return {
        "needs_debugging": answer == "YES"
    }