import numpy as np
from utils import read_file_lines

LEFT, RIGHT, UP, DOWN = "<", ">", "^", "v"
DIR_CHANGE = {LEFT: (0, -1), RIGHT: (0, 1), UP: (-1, 0), DOWN: (1, 0)}
SIGN_CHANGE = {LEFT: UP, UP: RIGHT, RIGHT: DOWN, DOWN: LEFT}


def main() -> None:
    # Process data
    content = read_file_lines("input/6_1.txt")
    content = [list("X" + line.strip() + "X") for line in content]
    empty_row = ["X" for _ in range(len(content[0]))]
    content.append(empty_row)
    content.insert(0, empty_row)

    n = len(content)
    m = len(content[0])
    step_taken = np.zeros((n, m))

    # Find the guard
    current_position = np.array((-1, -1))
    for i in range(n):
        if current_position[0] != -1:
            break
        for j in range(m):
            if content[i][j] in [LEFT, RIGHT, UP, DOWN]:
                current_position = np.array([i, j])
                break

    # Count her steps
    step_taken[current_position[0]][current_position[1]] = 1
    while True:
        current_position_value = content[current_position[0]][current_position[1]]
        next_position = current_position + DIR_CHANGE[current_position_value]
        next_position_value = content[next_position[0]][next_position[1]]
        if next_position_value == "#":
            # Change guard's direction
            content[current_position[0]][current_position[1]] = SIGN_CHANGE[current_position_value]
        elif next_position_value == "X":
            # Out of map
            break
        else:
            # Move the guard
            content[next_position[0]][next_position[1]] = current_position_value
            current_position = next_position
        step_taken[current_position[0]][current_position[1]] = 1

    print(int(step_taken.sum()))


if __name__ == "__main__":
    main()
