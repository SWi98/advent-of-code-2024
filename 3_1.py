if __name__ == "__main__":
    with open("input/3.txt", "r") as f:
        content = f.read()
    candidates = content.split("mul")
    res = 0
    for candidate in candidates:
        # print(candidate)
        if candidate[0] != "(":
            continue
        calculations = candidate.split(")")
        # print("Calcs:", calculations)
        if len(calculations) == 0:
            continue
        calculation = calculations[0][1:]
        numbers = calculation.split(",")
        if len(numbers) != 2:
            continue
        try:
            a, b = numbers
            a = int(a)
            b = int(b)
            res += a * b
        except Exception as e:
            continue
    print(res)
