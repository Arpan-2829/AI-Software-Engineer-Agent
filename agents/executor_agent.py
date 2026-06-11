from tools.python_tool import execute_python


def executor_agent(state):

    code = state["code"]

    result = execute_python(code)

    return {
    "execution_output": result["stdout"],
    "execution_error": result["stderr"],
    "current_agent": "executor"}