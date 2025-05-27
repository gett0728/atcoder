from collections import deque

h, w = map(int, input().split())
grid = []

direction = [(-1, 0, "v"), (1, 0, "^"), (0, -1, ">"), (0, 1, "<")] 
dist = [[-1] * w for _ in range(h)]
arrow = [[""] * w for _ in range(h)]

q = deque()

for i in range(h):
    s = input()
    grid.append(s)

    for j in range(w):
        if s[j] == "E":
            q.append((i, j))
            dist[i][j] = 0

while q:
    i, j = q.popleft()
    for dx, dy, dir in direction:
        x, y = i + dx, j + dy

        if (0 <= x < h) and (0 <= y < w) and (grid[x][y] == ".") and (dist[x][y] == -1):
            dist[x][y] = dist[i][j] + 1
            arrow[x][y] = dir
            q.append((x, y))

for i in range(h):
    ans = []
    for j in range(w):
        if grid[i][j] == ".":
            ans.append(arrow[i][j])
        else:
            ans.append(grid[i][j])
    print(*ans, sep="")