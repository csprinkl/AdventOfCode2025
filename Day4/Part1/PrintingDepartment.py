def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions for all 8 neighbors
    directions = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1),          (0,1),
        (1,-1), (1,0), (1,1)
    ]
    
    accessible = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            
            adjacent_rolls = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    adjacent_rolls += 1
            
            if adjacent_rolls < 4:
                accessible += 1
    
    return accessible


if __name__ == "__main__":
    # Load puzzle input
    with open("input.txt") as f:
        grid = [line.strip() for line in f]

    result = count_accessible_rolls(grid)
    print("Accessible rolls:", result)
