from numpy import sign

if __name__ == "__main__":
    with open("input/2.txt", "r") as f:
        content = f.readlines()
    res = 0
    for report in content:
        numbers = list(map(int, report.split()))
        safe = True
        for i in range(1, len(numbers)):
            prev = numbers[i - 1]
            curr = numbers[i]
            diff = curr - prev
            if i == 1:
                monotonicity = sign(diff)
                if monotonicity == 0:
                    safe = False
                    break
            if sign(diff) != monotonicity or abs(diff) > 3 or abs(diff) < 1:
                safe = False
                break
        res += 1 if safe else 0
    print(res)
