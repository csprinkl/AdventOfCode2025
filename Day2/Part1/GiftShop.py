# Reads puzzle input from input.txt and prints the sum of all invalid IDs.
# An ID is invalid if it is made of a sequence of digits repeated *exactly twice*.

def is_invalid(num_str: str) -> bool:
    """Return True if the string is made of a sequence of digits repeated twice."""
    if len(num_str) % 2 != 0:
        return False
    half = len(num_str) // 2
    return num_str[:half] == num_str[half:]


def main():
    with open("input.txt", "r") as f:
        raw = f.read().strip().replace("\n", "").replace(" ", "")

    ranges = raw.split(",")
    total = 0

    for r in ranges:
        if not r:
            continue

        start_str, end_str = r.split("-")
        start, end = int(start_str), int(end_str)

        for n in range(start, end + 1):
            if is_invalid(str(n)):
                total += n

    print("Sum of invalid IDs:", total)


if __name__ == "__main__":
    main()