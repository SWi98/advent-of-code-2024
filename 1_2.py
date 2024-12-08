if __name__ == "__main__":
    with open("input/1.txt", "r") as f:
        content = f.readlines()
    res = 0
    A, B = [], []
    for line in content:
        a, b = line.strip().split()
        A.append(int(a))
        B.append(int(b))
    B_dict = {}
    for b in B:
        B_dict[b] = B_dict.get(b, 0) + 1
    for a in A:
        res += a * B_dict.get(a, 0)
    print(res)
