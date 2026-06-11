import sys
import os
import time

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from agent_status import show_agent_status
import streamlit as st
from graph.builder import graph

st.set_page_config(
    page_title="AI Software Engineer Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Software Engineer Agent")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
task = st.chat_input(
    "Ask the AI Software Engineer..."
)

if task:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": task
        }
    )

    with st.chat_message("user"):
        st.markdown(task)

    # Assistant response
    with st.chat_message("assistant"):

        config = {
            "configurable": {
                "thread_id": "1"
            }
        }

        status_placeholder = st.empty()

        # Collect the complete state
        result = {}

        for event in graph.stream(
            {
                "task": task
            },
            config=config
        ):

            for node_name, state in event.items():

                status_placeholder.markdown(
                    show_agent_status(node_name)
                )

                result.update(state)

                time.sleep(1)  # Simulate processing time

        status_placeholder.success(
            "🎉 AI Software Engineer Finished!"
        )

        st.success("Completed Successfully!")

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
            [
                "📋 Plan",
                "💻 Code",
                "🧪 Tests",
                "📚 Docs",
                "⚙ Execution",
                "📂 Files"
            ]
        )

        with tab1:
            st.write(result.get("plan", ""))

        with tab2:

            code = result.get(
                "fixed_code",
                result.get("code", "")
            )

            st.code(
                code,
                language="python"
            )

            st.download_button(
                "Download main.py",
                code,
                file_name="main.py"
            )

        with tab3:

            st.code(
                result.get("tests", ""),
                language="python"
            )

            st.download_button(
                "Download test_main.py",
                result.get("tests", ""),
                file_name="test_main.py"
            )

        with tab4:

            st.write(
                result.get("documentation", "")
            )

            st.download_button(
                "Download README.md",
                result.get("documentation", ""),
                file_name="README.md"
            )

        with tab5:

            st.subheader("Execution Output")

            st.text(
                result.get(
                    "execution_output",
                    ""
                )
            )

            st.subheader("Execution Error")

            st.text(
                result.get(
                    "execution_error",
                    ""
                )
            )

        with tab6:

            st.subheader("📁 Generated Files")

            if "generated_files" in result:

                selected_file = st.selectbox(
                    "Choose a file",
                    result["generated_files"]
                )

                if selected_file:

                    st.success(selected_file)

                    with open(
                        selected_file,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content = f.read()

                    if selected_file.endswith(".py"):

                        st.code(
                            content,
                            language="python"
                        )

                    else:

                        st.text(content)

            else:

                st.warning(
                    "No files generated."
                )

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": "Task completed successfully."
        }
    )