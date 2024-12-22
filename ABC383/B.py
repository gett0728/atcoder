h, w, d = map(int, input().split())
grid = [input().strip() for _ in range(h)]
floor = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == '.']

def md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

result = 0

for i in range(len(floor)):
    for j in range(i + 1, len(floor)):
        x1, y1 = floor[i]
        x2, y2 = floor[j]
        humid = set()

        for a, b in floor:
            if md(x1, y1, a, b) <= d:
                humid.add((a, b))

        for a, b in floor:
            if md(x2, y2, a, b) <= d:
                humid.add((a, b))
        
        result = max(result, len(humid))

print(result)

