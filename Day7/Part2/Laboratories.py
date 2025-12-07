def solve_quantum_tachyon_splitting(manifold):
    """
    Calculates the total number of different timelines by counting the number of
    distinct paths from the starting point 'S' to the end of the manifold.

    This uses a Dynamic Programming approach (similar to a breadth-first search)
    to track how many timelines reach each cell.
    """
    if not manifold:
        return 0

    R = len(manifold)
    # Determine the maximum column width for a uniform grid
    C = max(len(row) for row in manifold) if manifold else 0

    # 1. Initialize the timeline count grid (DP table)
    # timeline_counts[y][x] stores the number of timelines reaching position (x, y).
    timeline_counts = [[0] * C for _ in range(R)]

    # 2. Locate the starting point 'S' and initialize its count to 1
    start_x, start_y = None, None
    for y in range(R):
        try:
            # Safely check the row content
            temp_row = manifold[y]
            if 'S' in temp_row:
                start_x = temp_row.index('S')
                start_y = y
                break
        except Exception:
            continue
    
    if start_x is None:
        return 0

    timeline_counts[start_y][start_x] = 1

    # 3. Simulate Timeline Progression (Dynamic Programming)
    # The particle moves only forward (down), from row 'y' to 'y+1'.
    for y in range(R):
        for x in range(C):
            current_timelines = timeline_counts[y][x]
            
            # Skip positions that have not been reached
            if current_timelines == 0:
                continue

            # Safely get cell content (handling rows shorter than C)
            cell = manifold[y][x] if x < len(manifold[y]) else ' '
            
            # --- Splitting Logic ---
            if cell == '^':
                # Quantum Split: Timelines reaching (x, y) split into two:
                # one goes left (x-1, y+1) and one goes right (x+1, y+1).
                next_y = y + 1
                
                if next_y < R:
                    # Path 1: Go Left (x-1)
                    next_x_left = x - 1
                    # Check bounds and ensure the target is not a wall '|'
                    is_valid_left = 0 <= next_x_left < C and (next_x_left >= len(manifold[next_y]) or manifold[next_y][next_x_left] != '|')
                    if is_valid_left:
                        timeline_counts[next_y][next_x_left] += current_timelines

                    # Path 2: Go Right (x+1)
                    next_x_right = x + 1
                    # Check bounds and ensure the target is not a wall '|'
                    is_valid_right = 0 <= next_x_right < C and (next_x_right >= len(manifold[next_y]) or manifold[next_y][next_x_right] != '|')
                    if is_valid_right:
                        timeline_counts[next_y][next_x_right] += current_timelines
            
            # --- Pass-Through Logic (Primarily for 'S') ---
            elif cell == 'S' or cell == '.':
                # The starting point 'S' and any empty path '.' must pass the count
                # down to the next row (y+1, x) unless it hits a wall.
                next_y = y + 1
                if next_y < R:
                    next_cell_content = manifold[next_y][x] if x < len(manifold[next_y]) else ' '
                    
                    # Pass the timeline count straight down to the same column
                    if next_cell_content != '|':
                        timeline_counts[next_y][x] += current_timelines


    # 4. Final Tally
    # The total number of timelines is the sum of all counts in the last row (R-1),
    # as any path reaching this row is considered a successful timeline.
    total_timelines = sum(timeline_counts[R - 1])

    return total_timelines

def load_input(file_path):
    """Loads and cleans the manifold map from the specified file."""
    try:
        with open(file_path, 'r') as file:
            # Read all non-empty, stripped lines
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found. Please ensure the manifold diagram is in the file.")
        # Return an empty list to prevent crash
        return []


if __name__ == "__main__":
    input_file = 'input.txt'
    manifold = load_input(input_file)
    
    # Calculate the total number of timelines
    total_timelines = solve_quantum_tachyon_splitting(manifold)
    
    print(f"The particle ends up on {total_timelines} different timelines.")