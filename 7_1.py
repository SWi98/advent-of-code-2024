import operator
from itertools import product

from utils import read_file_lines


def main() -> None:
    # Process data
    content = read_file_lines("input/7_1.txt")
    operators = (operator.add, operator.mul)
    total_sum = 0
    for line in content:
        result, numbers = line.strip().split(": ")
        numbers = list(map(int, numbers.split()))
        result = int(result)
        n = len(numbers)
        operators_variations = list(product(operators, repeat=(n - 1)))

        for operators_variation in operators_variations:
            current_operators_res = 0
            for i in range(n - 1):
                if i > 0:
                    current_operators_res = operators_variation[i](
                        current_operators_res, numbers[i + 1]
                    )
                else:
                    current_operators_res = operators_variation[i](numbers[i], numbers[i + 1])
            if current_operators_res == result:
                total_sum += result
                break
    print(total_sum)


if __name__ == "__main__":
    main()
