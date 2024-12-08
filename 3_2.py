if __name__ == "__main__":
    with open("input/3.txt", "r") as f:
        content = f.read()
    res = 0
    n = len(content)
    enabled = True
    for i in range(len(content)):
        print("--------")
        potential_do = content[i - 1 : i + 1]
        if i >= 1 and potential_do == "do":
            enabled = True
        potential_dont = content[i - 4 : i + 1]
        if i >= 4 and potential_dont == "don't":
            print("!!! FOUND DONT !!!")
            enabled = False
        potential_mul = content[i - 2 : i + 1]
        if i >= 2 and potential_mul == "mul" and enabled:
            print(content[: i + 1], content[i + 1 :], "FOUND MUL\n-----------")
            j = i + 1
            if content[j] == "(":
                while j < n:
                    j += 1
                    if content[j] == ")":
                        calculation = content[i + 2 : j]
                        numbers = calculation.split(",")
                        print(numbers)
                        if len(numbers) != 2:
                            break
                        try:
                            a, b = numbers
                            a = int(a)
                            b = int(b)
                            res += a * b
                            print("SUCCESS")
                        except Exception as e:
                            break
                        break
    print(res)
