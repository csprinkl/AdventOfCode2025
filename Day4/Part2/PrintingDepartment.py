def count_adjacent(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1),  (1,0),  (1,1)
    ]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            count += 1
    return count


def remove_accessible_rolls(grid):
    """
    Perform one removal wave:
    - Find all accessible rolls (@ with <4 adjacent @)
    - Remove them (set to '.')
    - Return number removed
    """
    rows, cols = len(grid), len(grid[0])
    to_remove = []

    # Find all removable rolls
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent(grid, r, c) < 4:
                    to_remove.append((r, c))

    # Remove them
    for r, c in to_remove:
        grid[r][c] = '.'

    return len(to_remove)


def total_removable_rolls(grid):
    total_removed = 0

    while True:
        removed = remove_accessible_rolls(grid)
        if removed == 0:
            break
        total_removed += removed

    return total_removed


if __name__ == "__main__":
    # Load puzzle input
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f]

    result = total_removable_rolls(grid)
    print("Total rolls removed:", result)
