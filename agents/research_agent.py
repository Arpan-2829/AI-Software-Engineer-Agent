from llm import llm
from tools.search_tool import search_web


def research_agent(state):

    task = state["task"]

    search_results = search_web(task)

    prompt = f"""
You are a research assistant.

Task:

{task}

Search Results:

{search_results}

Provide useful technical information.
"""

    response = llm.invoke(prompt)

    return {
        "research": response.content
    }