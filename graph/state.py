from typing import TypedDict, List


class AgentState(TypedDict):
    task: str
    research: str
    plan: str
    code: str
    fixed_code: str
    tests: str
    documentation: str
    execution_output: str
    execution_error: str
    needs_debugging: bool
    approved: bool
    generated_files: list