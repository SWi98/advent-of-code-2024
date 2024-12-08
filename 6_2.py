from copy import deepcopy

import numpy as np
from tqdm import tqdm
from utils import read_file_lines

LEFT, RIGHT, UP, DOWN = "<", ">", "^", "v"
DIR_CHANGE = {LEFT: (0, -1), RIGHT: (0, 1), UP: (-1, 0), DOWN: (1, 0)}
SIGN_CHANGE = {LEFT: UP, UP: RIGHT, RIGHT: DOWN, DOWN: LEFT}


def is_cycled(content: list[list[str]], current_position: np.ndarray) -> bool:
    visited = set()
    visited.add((*current_position, content[current_position[0]][current_position[1]]))
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
        position_id = (
            *current_position,
            content[current_position[0]][current_position[1]],
        )
        if position_id in visited:
            return True
        visited.add((*current_position, content[current_position[0]][current_position[1]]))
    return False


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
    initial_position = np.array((-1, -1))
    for i in range(n):
        if initial_position[0] != -1:
            break
        for j in range(m):
            if content[i][j] in [LEFT, RIGHT, UP, DOWN]:
                initial_position = np.array([i, j])
                break

    # Calculate the route
    current_position = initial_position
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
    visited_positions = np.where(step_taken == 1)
    total = len(visited_positions[0])

    count = 0
    for position in tqdm(zip(visited_positions[0], visited_positions[1]), total=total):
        if np.all(position == initial_position):
            continue
        new_content = deepcopy(content)
        new_content[position[0]][position[1]] = "#"
        if is_cycled(new_content, initial_position):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
