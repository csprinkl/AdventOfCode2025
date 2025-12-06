def read_ranges(path):
    with open(path) as f:
        sections = f.read().strip().split("\n\n")
    range_lines = sections[0].splitlines()

    ranges = []
    for line in range_lines:
        a, b = map(int, line.split("-"))
        ranges.append((a, b))

    return ranges

def merge_intervals(ranges):
    """Merge overlapping or touching intervals."""
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1] + 0:
            # No overlap
            merged.append([start, end])
        else:
            # Overlap → merge
            merged[-1][1] = max(merged[-1][1], end)

    return merged

if __name__ == "__main__":
    ranges = read_ranges("input.txt")
    merged = merge_intervals(ranges)

    # Count total distinct covered IDs
    total_fresh = sum(end - start + 1 for start, end in merged)
    print("Total fresh IDs covered by ranges:", total_fresh)

