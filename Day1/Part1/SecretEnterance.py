def solve(filename: str) -> int:
    pos = 50               # starting position
    count_zero = 0         # number of times dial lands on 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            steps = int(line[1:])

            if direction == "L":
                pos = (pos - steps) % 100
            elif direction == "R":
                pos = (pos + steps) % 100
            else:
                raise ValueError(f"Invalid instruction: {line}")

            if pos == 0:
                count_zero += 1

    return count_zero


if __name__ == "__main__":
    # Change "input.txt" to your input file name
    result = solve("input.txt")
    print("Password:", result)