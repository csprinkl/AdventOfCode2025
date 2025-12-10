import math
from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def solve(filename):
    # Read 3D points
    points = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y, z = map(int, line.split(","))
                points.append((x, y, z))

    n = len(points)
    uf = UnionFind(n)

    # Build all edges
    edges = []
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
        edges.append((d2, i, j))

    edges.sort()

    # Process edges in increasing distance
    for d2, a, b in edges:
        merged = uf.union(a, b)

        # When the LAST merge happens (components → 1)
        if merged and uf.components == 1:
            x1 = points[a][0]
            x2 = points[b][0]
            product = x1 * x2
            print("Last connection:", points[a], points[b])
            print("X-coordinates:", x1, x2)
            print("Product:", product)
            return


if __name__ == "__main__":
    solve("input.txt")
