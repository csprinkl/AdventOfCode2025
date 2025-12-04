def max_joltage_for_bank(bank: str) -> int:
    """
    Given a string of digits (a battery bank), return the largest two-digit
    number that can be formed by choosing two digits in order.
    """
    digits = bank.strip()
    best = -1
    n = len(digits)

    for i in range(n):
        for j in range(i + 1, n):
            val = int(digits[i] + digits[j])
            if val > best:
                best = val
    return best


def total_output_joltage(lines):
    total = 0
    per_bank = []

    for line in lines:
        if line.strip() == "":
            continue
        m = max_joltage_for_bank(line)
        per_bank.append(m)
        total += m

    return per_bank, total


if __name__ == "__main__":
    # Read from input.txt
    with open("input.txt", "r") as f:
        data = f.read().strip().splitlines()

    per_bank, total = total_output_joltage(data)

    for i, val in enumerate(per_bank, 1):
        print(f"Bank {i}: {val}")
    print("Total output joltage:", total)