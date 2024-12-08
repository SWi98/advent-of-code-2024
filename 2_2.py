from numpy import sign


def check_safety(numbers: list[int]) -> bool:
    safe = True
    for i in range(1, len(numbers)):
        prev = numbers[i - 1]
        curr = numbers[i]
        diff = curr - prev
        if i == 1:
            monotonic = sign(diff)
            if monotonic == 0:
                safe = False
                break
        if sign(diff) != monotonic or abs(diff) > 3 or abs(diff) < 1:
            safe = False
            break
    return safe


if __name__ == "__main__":
    with open("input/2.txt", "r") as f:
        content = f.readlines()
    res = 0
    for report in content:
        numbers = list(map(int, report.split()))
        safe = True
        for i in range(len(numbers)):
            new_numbers = numbers.copy()
            del new_numbers[i]
            is_safe = check_safety(new_numbers)
            if is_safe:
                safe = True
                break
            else:
                safe = False
        res += 1 if safe else 0
    print(res)
