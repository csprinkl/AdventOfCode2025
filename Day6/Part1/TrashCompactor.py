import math

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]

def transpose(lines):
    """Turn list of text lines into list of columns."""
    width = max(len(l) for l in lines)
    padded = [l.ljust(width) for l in lines]
    return list(map(list, zip(*padded)))  # list of columns

def split_into_problems(columns):
    """Group consecutive non-blank columns into problem blocks."""
    problems = []
    current = []

    for col in columns:
        if all(c == ' ' for c in col):
            if current:
                problems.append(current)
                current = []
        else:
            current.append(col)

    if current:
        problems.append(current)

    return problems

def parse_problem(problem_cols):
    """
    Extract:
      - numbers (on rows above the operator)
      - operator (last non-space row)
    """
    rows = list(map(''.join, zip(*problem_cols)))

    # Find operator row (bottom-most non-empty)
    for i in range(len(rows)-1, -1, -1):
        s = rows[i].strip()
        if s:
            operator = s
            operator_row = i
            break

    # All rows above operator are numbers
    numbers = [int(r.strip()) for r in rows[:operator_row] if r.strip()]

    return numbers, operator

def compute(numbers, op):
    if op == '+':
        return sum(numbers)
    elif op == '*':
        return math.prod(numbers)
    else:
        raise ValueError(f"Unknown operator {op}")

if __name__ == "__main__":
    lines = read_input("input.txt")
    columns = transpose(lines)
    problems = split_into_problems(columns)

    total = 0
    for p in problems:
        nums, op = parse_problem(p)
        total += compute(nums, op)

    print(total)
