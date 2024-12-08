def read_file_lines(path: str) -> list[str]:
    with open(path, "r") as f:
        content = f.readlines()
    return content
