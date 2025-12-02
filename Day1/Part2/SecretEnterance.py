def solve(filename: str) -> int:
    pos = 50  # starting position
    count_zero = 0

    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            steps = int(line[1:])

            # Normalize steps to 0–99 cycles for counting full revolutions
            full_revs = steps // 100
            remainder = steps % 100

            # Every full revolution hits 0 exactly once
            count_zero += full_revs

            # Determine click direction
            if direction == "L":
                step_dir = -1
            elif direction == "R":
                step_dir = +1
            else:
                raise ValueError(f"Invalid instruction: {line}")

            # Check "remainder" steps for passes over 0
            current = pos
            for _ in range(remainder):
                current = (current + step_dir) % 100
                if current == 0:
                    count_zero += 1

            # Final position after full rotation
            pos = (pos + step_dir * remainder) % 100

    return count_zero


if __name__ == "__main__":
    result = solve("input.txt")
    print("Password:", result)
