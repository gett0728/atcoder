n = int(input())
grid_s = [list(input()) for _ in range(n)]
grid_t = [list(input()) for _ in range(n)]

def rotate(grid):
    return [[grid[n-j-1][i] for j in range(n)] for i in range(n)]

ans = float("inf")

for spin in range(4):
    temp = 0

    for i in range(n):
        for j in range(n):
            if grid_s[i][j] != grid_t[i][j]:
                temp += 1

    ans = min(ans, spin + temp)
    grid_s = rotate(grid_s)

print(ans)