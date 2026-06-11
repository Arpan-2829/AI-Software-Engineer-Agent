import subprocess
import tempfile


def execute_python(code: str):

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".py",
        delete=False
    ) as temp:

        temp.write(code)

        file_path = temp.name

    result = subprocess.run(
        ["python", file_path],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }