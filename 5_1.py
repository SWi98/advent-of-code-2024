from enum import Enum


class NumberOrder(Enum):
    NOT_EXIST = "NOT_EXIST"
    AFTER_CURRENT = "AFTER_CURRENT"
    BEFORE_CURRENT = "BEFORE_CURRENT"


if __name__ == "__main__":
    with open("input/5_1.txt", "r") as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    rules = {i: set() for i in range(0, 101)}
    i = 0
    while content[i] != "":
        num_before, rul_number = list(map(int, content[i].split("|")))
        rules[rul_number].add(num_before)
        i += 1
    i += 1
    res = 0
    while i < len(content):
        sequence = list(map(int, content[i].split(",")))
        numbers_ordering = [
            NumberOrder.NOT_EXIST if i not in sequence else NumberOrder.AFTER_CURRENT
            for i in range(0, 101)
        ]
        good_sequence = True
        for j in range(0, len(sequence)):
            current = sequence[j]
            if j > 0:
                previous = sequence[j - 1]
                numbers_ordering[previous] = NumberOrder.BEFORE_CURRENT
            for num_has_to_be_before in rules[current]:
                if not (
                    (numbers_ordering[num_has_to_be_before] == NumberOrder.NOT_EXIST)
                    or (numbers_ordering[num_has_to_be_before] == NumberOrder.BEFORE_CURRENT)
                ):
                    good_sequence = False
                    break
            if not good_sequence:
                break
        if good_sequence:
            middle_element_idx = int((len(sequence)) / 2)
            res += sequence[middle_element_idx]
        i += 1
    print(res)
