def max_k_digits(bank: str, k: int) -> str:
    """
    Select exactly k digits from `bank` to form the largest possible number,
    preserving original order.
    """
    digits = bank.strip()
    drops = len(digits) - k  # how many digits we are allowed to discard
    stack = []

    for d in digits:
        while drops > 0 and stack and stack[-1] < d:
            stack.pop()
            drops -= 1
        stack.append(d)

    # If we didn't drop enough, cut the tail
    return "".join(stack[:k])


def total_output_joltage(lines):
    total = 0
    per_bank = []

    for line in lines:
        if not line.strip():
            continue
        chosen = max_k_digits(line, 12)
        per_bank.append(chosen)
        total += int(chosen)

    return per_bank, total


if __name__ == "__main__":
    # Read from input.txt
    with open("input.txt", "r") as f:
        data = f.read().strip().splitlines()

    per_bank, total = total_output_joltage(data)

    for i, val in enumerate(per_bank, 1):
        print(f"Bank {i}: {val}")
    print("\nTotal output joltage:", total)
