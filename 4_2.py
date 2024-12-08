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
            if content[i, j] == "A":
                diag_one = (content[i - 1, j - 1], content[i + 1, j + 1])
                diag_two = (content[i + 1, j - 1], content[i - 1, j + 1])
                if (diag_one == ("M", "S") or diag_one == ("S", "M")) and (
                    diag_two == ("M", "S") or diag_two == ("S", "M")
                ):
                    res += 1
    print(res)
