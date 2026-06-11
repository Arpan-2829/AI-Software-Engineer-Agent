import os


def save_file(filename, content):

    os.makedirs("outputs", exist_ok=True)

    path = os.path.join(
        "outputs",
        filename
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return path