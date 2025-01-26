h, w = map(int, input().split())
grid = []

for i in range(h):
    s = list(input())
    grid.append(s)

min_row, max_row = h, -1
min_col, max_col = w, -1

for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

is_possible = True

for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        if grid[i][j] == ".":
            is_possible = False
            break
    if not is_possible:
        break

if is_possible:
    print("Yes")
else:
    print("No")
