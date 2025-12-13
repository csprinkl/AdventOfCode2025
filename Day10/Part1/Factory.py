import itertools
import re

def parse_line(line):
    # Indicator diagram
    diagram = re.search(r"\[([.#]+)\]", line).group(1)
    target = [1 if c == "#" else 0 for c in diagram]
    num_lights = len(target)

    # Button definitions
    buttons = []
    for group in re.findall(r"\((.*?)\)", line):
        if group.strip() == "":
            buttons.append([])
        else:
            buttons.append(list(map(int, group.split(","))))

    return target, num_lights, buttons


def min_presses_for_machine(target, num_lights, buttons):
    m = len(buttons)
    best = float("inf")

    # Try all subsets of buttons
    for mask in range(1 << m):
        lights = [0] * num_lights
        presses = 0

        for i in range(m):
            if mask & (1 << i):
                presses += 1
                for light in buttons[i]:
                    lights[light] ^= 1

        if lights == target:
            best = min(best, presses)

    return best


if __name__ == "__main__":
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            target, num_lights, buttons = parse_line(line)
            total += min_presses_for_machine(
                target, num_lights, buttons
            )

    print(total)
