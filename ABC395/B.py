n = int(input())

grid = [["?"] * n for _ in range(n)]

for i in range(n):
    j = n - i - 1
    if i <= j:
        for x in range(i, j+1):
            for y in range(i, j+1):
                if i % 2 == 0:
                    grid[x][y] = "#"
                else:
                    grid[x][y] = "."

for i in grid:
    print("".join(i))