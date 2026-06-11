def show_agent_status(current_agent):

    agents = [
        "research",
        "planner",
        "coder",
        "executor",
        "reviewer",
        "debugger",
        "human_review",
        "tester",
        "docs",
        "file_writer"
    ]

    output = "## 🤖 Agent Execution\n\n"

    current_index = agents.index(current_agent)

    for i, agent in enumerate(agents):

        if i < current_index:

            output += f"✅ **{agent}** Completed\n\n"

        elif i == current_index:

            output += f"🟢 **{agent}** Running...\n\n"

        else:

            output += f"⏳ **{agent}** Waiting\n\n"

    return output