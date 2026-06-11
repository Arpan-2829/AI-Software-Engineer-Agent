from langgraph.graph import StateGraph, START, END
from agents.research_agent import research_agent
from memory.memory import memory
from graph.state import AgentState
from agents.file_writer_agent import file_writer_agent
from agents.planner_agent import planner_agent
from agents.coder_agent import coder_agent
from agents.executor_agent import executor_agent
from agents.reviewer_agent import reviewer_agent
from agents.debugger_agent import debugger_agent
from agents.tester_agent import tester_agent
from agents.docs_agent import docs_agent
from agents.human_review_agent import human_review_agent


# Create graph
builder = StateGraph(AgentState)


# ==========================
# Add Nodes
# ==========================
builder.add_node("planner", planner_agent)
builder.add_node("coder", coder_agent)
builder.add_node("executor", executor_agent)
builder.add_node("reviewer", reviewer_agent)
builder.add_node("debugger", debugger_agent)
builder.add_node("human_review", human_review_agent)
builder.add_node("tester", tester_agent)
builder.add_node("docs", docs_agent)
builder.add_node("file_writer",file_writer_agent)
builder.add_node("research",research_agent)


# ==========================
# Router Functions
# ==========================
def route_debug(state):

    if state["needs_debugging"]:
        return "debugger"

    return "human_review"


def approval_router(state):

    if state["approved"]:
        return "tester"

    return "coder"


# ==========================
# Edges
# ==========================
builder.add_edge(START, "research")

builder.add_edge("research", "planner")

builder.add_edge("planner", "coder")

builder.add_edge("coder", "executor")

builder.add_edge("executor", "reviewer")


# ==========================
# Reviewer Decision
# ==========================
builder.add_conditional_edges(
    "reviewer",
    route_debug,
    {
        "debugger": "debugger",
        "human_review": "human_review"
    }
)


# ==========================
# Debugger → Human Review
# ==========================
builder.add_edge(
    "debugger",
    "human_review"
)

# ==========================
# Human Approval
# ==========================
builder.add_conditional_edges(
    "human_review",
    approval_router,
    {
        "tester": "tester",
        "coder": "coder"
    }
)


# ==========================
# Final Flow
# ==========================
builder.add_edge("tester", "docs")

builder.add_edge(
    "docs",
    "file_writer"
)

builder.add_edge(
    "file_writer",
    END
)


# ==========================
# Compile Graph
# ==========================
graph = builder.compile(
    checkpointer=memory
)