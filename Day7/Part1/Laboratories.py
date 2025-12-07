def simulate_tachyon_beam(manifold):
    # Locate the starting point 'S'
    start_x, start_y = None, None
    for y, row in enumerate(manifold):
        if 'S' in row:
            start_x = row.index('S')
            start_y = y
            break

    # Beam will initially move down from the starting point just below 'S'
    beams = [(start_x, start_y + 1)]  # store beams as (x, y) positions
    split_count = 0
    visited = set()  # To avoid re-processing the same beam position

    while beams:
        new_beams = []  # Holds new beams created in the current iteration
        for x, y in beams:
            # If the beam is out of bounds, skip it
            if y >= len(manifold) or x < 0 or x >= len(manifold[y]):
                continue

            # If we've already processed this cell, skip it
            if (x, y) in visited:
                continue

            visited.add((x, y))  # Mark this position as visited

            cell = manifold[y][x]
            
            if cell == '^':
                # Splitter found: increment split count
                split_count += 1
                # Add two new beams: one left and one right of the splitter
                if x - 1 >= 0 and manifold[y][x - 1] != '^':
                    new_beams.append((x - 1, y + 1))  # Beam goes left
                if x + 1 < len(manifold[y]) and manifold[y][x + 1] != '^':
                    new_beams.append((x + 1, y + 1))  # Beam goes right
            elif cell == '.':
                # Empty space: continue moving down
                new_beams.append((x, y + 1))

        # Update the beams to process in the next iteration
        beams = new_beams

    return split_count

def load_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    input_file = 'input.txt'
    manifold = load_input(input_file)
    
    total_splits = simulate_tachyon_beam(manifold)
    
    print(f"The beam was split {total_splits} times.")