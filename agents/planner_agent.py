from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from llm import llm


def planner_agent(state):
    task = state["task"]
    research = state["research"]

    prompt = f"""
        You are a senior software architect.

        Task:

        {task}

        Research Information:

        {research}

        Using the research information above,
        create a detailed step-by-step plan.

        Be technical and specific.
        """

    response = llm.invoke(prompt)

    return {
    "plan": response.content,
    "current_agent": "planner"}