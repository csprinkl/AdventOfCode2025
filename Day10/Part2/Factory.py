def subsets(n):
    if n == 0:
        yield ()
        return
    for rest in subsets(n - 1):
        yield rest + (0,)
        yield rest + (1,)


def min_presses_for_machine(target, buttons):
    num_counters = len(target)

    ops = {}
    patterns = {}

    # Precompute button subsets
    for pressed in subsets(len(buttons)):
        counters = [0] * num_counters

        for i in range(len(pressed)):
            if pressed[i]:
                for idx in buttons[i]:
                    counters[idx] += 1

        parity = tuple(x & 1 for x in counters)
        ops[pressed] = tuple(counters)
        patterns.setdefault(parity, []).append(pressed)

    memo = {}

    def solve(curr_target):
        if curr_target in memo:
            return memo[curr_target]

        if all(x == 0 for x in curr_target):
            return 0
        if any(x < 0 for x in curr_target):
            return float("inf")

        parity = tuple(x & 1 for x in curr_target)
        best = float("inf")

        for pressed in patterns.get(parity, []):
            diff = ops[pressed]
            next_target = tuple(
                (curr_target[i] - diff[i]) // 2
                for i in range(num_counters)
            )

            cost = sum(pressed) + 2 * solve(next_target)
            best = min(best, cost)

        memo[curr_target] = best
        return best

    return solve(target)


if __name__ == "__main__":
    total = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            _, *buttons, jolts = line.split()

            buttons = [
                tuple(int(x) for x in b[1:-1].split(","))
                for b in buttons
            ]

            target = tuple(
                int(x) for x in jolts[1:-1].split(",")
            )

            total += min_presses_for_machine(target, buttons)

    print(total)
