import math

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        return [line.rstrip("\n") for line in f.readlines()]

def transpose(lines):
    """Convert text lines to list-of-columns (list of char lists)."""
    width = max(len(l) for l in lines)
    padded = [l.ljust(width) for l in lines]
    return list(map(list, zip(*padded)))

def split_into_problems(columns):
    """Group consecutive non-space columns into problem blocks."""
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

def parse_problem_part2(problem_cols):
    """
    Rules:
      - Numbers are read RIGHT-TO-LEFT one column at a time
      - Within a column, top digit = most significant, bottom = least
      - Operator is bottom-most non-space cell in the entire block
    """
    # First find the operator row (bottom-most nonempty row across the whole block)
    height = len(problem_cols[0])
    operator_row = None
    operator = None

    for r in range(height - 1, -1, -1):
        # check if any column has a non-space on this row
        for col in problem_cols:
            if col[r] != ' ':
                # If this is an operator, it will be the LAST non-space in the block.
                # Since this is bottom-up, the first one we hit is the operator.
                # Check if it's a symbol:
                if col[r] in "+*":
                    operator = col[r]
                    operator_row = r
                break
        if operator_row is not None:
            break

    if operator is None:
        raise ValueError("Operator not found in problem block")

    # Now read each number column, RIGHT to LEFT
    numbers = []
    for col in reversed(problem_cols):
        digits = [col[r] for r in range(operator_row) if col[r].isdigit()]
        if digits:
            numbers.append(int("".join(digits)))

    return numbers, operator

def compute(numbers, op):
    return sum(numbers) if op == "+" else math.prod(numbers)

if __name__ == "__main__":
    lines = read_input("input.txt")
    columns = transpose(lines)
    problems = split_into_problems(columns)

    total = 0
    for p in problems:
        nums, op = parse_problem_part2(p)
        total += compute(nums, op)
    print(total)
