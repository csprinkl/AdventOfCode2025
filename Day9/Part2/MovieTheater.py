# Compute rectangle area
def rect_area(a, b):
    return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))

# Check if rectangle intersects any polygon segment
def intersects(rect_corner1, rect_corner2, segments):
    rx1, ry1 = rect_corner1
    rx2, ry2 = rect_corner2
    min_x = min(rx1, rx2)
    max_x = max(rx1, rx2)
    min_y = min(ry1, ry2)
    max_y = max(ry1, ry2)

    for seg in segments:
        (sx1, sy1), (sx2, sy2) = seg
        if sx1 == sx2:  # vertical segment
            x = sx1
            y_min_seg = min(sy1, sy2)
            y_max_seg = max(sy1, sy2)
            if min_x < x < max_x and max(y_min_seg, min_y) < min(y_max_seg, max_y):
                return True
        elif sy1 == sy2:  # horizontal segment
            y = sy1
            x_min_seg = min(sx1, sx2)
            x_max_seg = max(sx1, sx2)
            if min_y < y < max_y and max(x_min_seg, min_x) < min(x_max_seg, max_x):
                return True
    return False

# Build segments from consecutive tiles (wrapping around)
def build_segments(tiles):
    segments = []
    n = len(tiles)
    for i in range(n):
        a = tiles[i]
        b = tiles[(i + 1) % n]  # wrap around
        segments.append((a, b))
    return segments

def solve(filename):
    # Read red tile coordinates
    tiles = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.split(","))
                tiles.append((x, y))

    segments = build_segments(tiles)
    max_area = 0

    # Check all pairs of red tiles
    n = len(tiles)
    for i in range(n):
        for j in range(i + 1, n):
            a = tiles[i]
            b = tiles[j]
            if not intersects(a, b, segments):
                area = rect_area(a, b)
                if area > max_area:
                    max_area = area

    print("Largest rectangle area with red/green tiles:", max_area)

if __name__ == "__main__":
    solve("input.txt")
