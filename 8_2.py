import numpy as np
from utils import read_file_lines


def try_add(X: np.ndarray, antinode: np.ndarray, parent: np.ndarray) -> None:
    n, m = X.shape
    X[parent[0], parent[1]] = 1
    while True:
        a, b = antinode
        if 0 <= a < n and 0 <= b < m:
            X[a, b] = 1
        else:
            break
        antinode, parent = 2 * antinode - parent, antinode


def main() -> None:
    content = read_file_lines("input/8_1.txt")
    content = np.array([list(line.strip()) for line in content])
    n, m = content.shape
    antinodes = np.zeros((n, m))
    antennas = {}
    for i in range(n):
        for j in range(m):
            symbol = content[(i, j)]
            if symbol != ".":
                antennas[str(symbol)] = antennas.get(str(symbol), [])
                antennas[str(symbol)].append(np.array((i, j)))
    for antenna, antenna_positions in antennas.items():
        print("WORKING ON", antenna)
        p = len(antenna_positions)
        for i in range(0, p - 1):
            curr = antenna_positions[i]
            for j in range(i + 1, p):
                neighbor = antenna_positions[j]
                # formula from wikipedia https://en.wikipedia.org/wiki/Point_reflection
                antinode_a = 2 * neighbor - curr
                antinode_b = 2 * curr - neighbor
                try_add(antinodes, antinode_a, parent=neighbor)
                try_add(antinodes, antinode_b, parent=curr)
    print(antinodes.sum())


if __name__ == "__main__":
    main()
