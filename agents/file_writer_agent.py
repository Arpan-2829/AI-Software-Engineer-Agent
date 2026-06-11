from tools.file_tool import save_file


def file_writer_agent(state):

    files = []

    # Save code
    code_path = save_file(
    "main.py",
    state.get(
        "fixed_code",
        state["code"]
    ))
    files.append(code_path)

    # Save tests
    test_path = save_file(
        "test_main.py",
        state.get(
            "tests",
            ""
        )
    )
    files.append(test_path)

    # Save documentation
    readme_path = save_file(
        "README.md",
        state.get(
            "documentation",
            ""
        )
    )
    files.append(readme_path)

    return {
        "generated_files": files
    }