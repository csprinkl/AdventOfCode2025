def read_input(path):
    with open(path) as f:
        sections = f.read().strip().split("\n\n")
    range_lines = sections[0].splitlines()
    id_lines = sections[1].splitlines()

    ranges = []
    for line in range_lines:
        a, b = map(int, line.split("-"))
        ranges.append((a, b))

    ids = [int(x) for x in id_lines]
    return ranges, ids

def is_fresh(ingredient_id, ranges):
    for a, b in ranges:
        if a <= ingredient_id <= b:
            return True
    return False

if __name__ == "__main__":
    ranges, ingredient_ids = read_input("input.txt")
    fresh_count = sum(is_fresh(i, ranges) for i in ingredient_ids)
    print("Fresh ingredient count:", fresh_count)
