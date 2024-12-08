from queue import Queue

import attr
import numpy as np

NEXT_SIGN = {"X": "M", "M": "A", "A": "S"}


def neighbors(location: tuple[int, int]) -> list[tuple[int, int]]:
    res = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0:
                continue
            res.append((location[0] + i, location[1] + j))
    return res


def bfs(x: np.ndarray, location: tuple[int, int]) -> int:
    q = Queue()
    found_words = 0
    current_element = (*location, -1, -1)
    q.put(current_element)
    visited = set([current_element])
    while not q.empty():
        i, j, prev_i, prev_j = q.get()
        current_sign = x[i, j]
        if x[i, j] == "S":
            print(i, j, prev_i, prev_j, x[prev_i, prev_j])
            found_words += 1
        else:
            for neighbor in neighbors((i, j)):
                new_i, new_j = neighbor
                new_sign = x[new_i, new_j]
                if (NEXT_SIGN[current_sign] == new_sign) and ((new_i, new_j) not in visited):
                    q.put((*neighbor, i, j))
                    if new_i == 3 and new_j == 5:
                        print("ADDING TO SET: 3,5")
                    visited.add((new_i, new_j))
    return found_words


if __name__ == "__main__":
    with open("input/4_test_1.txt", "r") as f:
        content = f.readlines()
    content = [list("." + line.strip() + ".") for line in content]
    empty_row = ["." for _ in range(len(content[0]))]
    content.append(empty_row)
    content.insert(0, empty_row)
    content = np.array(content)
    n, m = content.shape
    res = 0
    for i in range(n):
        for j in range(m):
            if content[i, j] == "X":
                print("BFS ON:", i, j)
                res += bfs(content, (i, j))
    print(res)
