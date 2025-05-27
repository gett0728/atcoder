h, w = map(int, input().split())
grid = []

for _ in range(h):
    a = list(map(int, input().split()))
    grid.append(a)

ans = 0
stack = []

stack.append((0, 0, [[0]*w for _ in range(h)]))

while stack:
    i, j, visited = stack.pop()

    if i == h:
        score = 0

        for y in range(h):
            for x in range(w):
                if not visited[y][x]:
                    score ^= grid[y][x]

        ans = max(ans, score)
        continue

    if j+1 < w:
        ni, nj = (i, j+1)
    else:
        ni, nj = (i+1, 0)

    stack.append((ni, nj, [k[:] for k in visited]))

    if (j+1 < w) and (not visited[i][j]) and (not visited[i][j+1]):
        new_visited = [k[:] for k in visited]
        new_visited[i][j] = 1
        new_visited[i][j+1] = 1
        stack.append((ni, nj, new_visited))

    if (i+1 < h) and (not visited[i][j]) and (not visited[i+1][j]):
        new_visited = [k[:] for k in visited]
        new_visited[i][j] = 1
        new_visited[i+1][j] = 1
        stack.append((ni, nj, new_visited))

print(ans)