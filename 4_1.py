import numpy as np

if __name__ == "__main__":
    with open("input/4_1.txt", "r") as f:
        content = f.readlines()
    content = [list("..." + line.strip() + "...") for line in content]
    for i in range(3):
        empty_row = ["." for _ in range(len(content[0]))]
        content.append(empty_row)
        content.insert(0, empty_row)
    content = np.array(content)
    n, m = content.shape
    res = 0
    print(content)
    for i in range(n):
        for j in range(m):
            if content[i, j] == "X":
                candidates = (
                    (content[i + 1, j], content[i + 2, j], content[i + 3, j]),  # down
                    (content[i - 1, j], content[i - 2, j], content[i - 3, j]),  # up
                    (
                        content[i + 1, j + 1],
                        content[i + 2, j + 2],
                        content[i + 3, j + 3],
                    ),  # down right
                    (
                        content[i + 1, j - 1],
                        content[i + 2, j - 2],
                        content[i + 3, j - 3],
                    ),  # down left
                    (
                        content[i - 1, j + 1],
                        content[i - 2, j + 2],
                        content[i - 3, j + 3],
                    ),  # up right
                    (
                        content[i - 1, j - 1],
                        content[i - 2, j - 2],
                        content[i - 3, j - 3],
                    ),  # up left
                    (content[i, j - 1], content[i, j - 2], content[i, j - 3]),  # left
                    (content[i, j + 1], content[i, j + 2], content[i, j + 3]),  # right
                )
                for candidate in candidates:
                    if candidate == ("M", "A", "S"):
                        res += 1
    print(res)
