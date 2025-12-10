def solve(filename):
    points = []

    # Read all red tile coordinates
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.split(","))
                points.append((x, y))

    max_area = 0
    n = len(points)

    # Compare each pair once
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            area = width * height

            if area > max_area:
                max_area = area

    print("Largest rectangle area:", max_area)


if __name__ == "__main__":
    solve("input.txt")
