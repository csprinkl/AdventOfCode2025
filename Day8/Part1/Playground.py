import math
from itertools import combinations

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # same component
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def solve(filename, K=1000):
    # Load coordinates
    points = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y, z = map(int, line.split(","))
                points.append((x, y, z))

    n = len(points)
    uf = UnionFind(n)

    # Build all pairwise distances (squared)
    edges = []
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        d2 = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
        edges.append((d2, i, j))

    # Sort all edges by distance
    edges.sort()

    # Process exactly K shortest edges (even if union does nothing)
    for idx in range(K):
        _, a, b = edges[idx]
        uf.union(a, b)   # union may or may not change structure

    # Count component sizes
    comp_sizes = {}
    for i in range(n):
        r = uf.find(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1

    largest = sorted(comp_sizes.values(), reverse=True)

    # Always ensure at least three entries
    while len(largest) < 3:
        largest.append(1)

    result = largest[0] * largest[1] * largest[2]

    print("Three largest circuit sizes:", largest[:3])
    print("Product:", result)

if __name__ == "__main__":
    solve("input.txt", K=1000)
