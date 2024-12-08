if __name__ == "__main__":
    with open("input/1.txt", "r") as f:
        content = f.readlines()
    res = 0
    A, B = [], []
    for line in content:
        a, b = line.strip().split()
        A.append(int(a))
        B.append(int(b))
    A.sort()
    B.sort()
    for a, b in zip(A, B):
        print(a, b)
        res += abs(b - a)
    print(res)
