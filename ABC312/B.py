n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

for i in range(n-8):
    for j in range(m-8):
        if grid[i][j] == "#":
            if all([
                grid[i][j] == "#",
                grid[i][j+1] == "#",
                grid[i][j+2] == "#",
                grid[i][j+3] == ".",

                grid[i+1][j] == "#",
                grid[i+1][j+1] == "#",
                grid[i+1][j+2] == "#",
                grid[i+1][j+3] == ".",

                grid[i+2][j] == "#",
                grid[i+2][j+1] == "#",
                grid[i+2][j+2] == "#",
                grid[i+2][j+3] == ".",
                
                grid[i+3][j] == ".",
                grid[i+3][j+1] == ".",
                grid[i+3][j+2] == ".",
                grid[i+3][j+3] == ".",

                grid[i+5][j+5] == ".",
                grid[i+5][j+6] == ".",
                grid[i+5][j+7] == ".",
                grid[i+5][j+8] == ".",

                grid[i+6][j+5] == ".",
                grid[i+6][j+6] == "#",
                grid[i+6][j+7] == "#",
                grid[i+6][j+8] == "#",

                grid[i+7][j+5] == ".",
                grid[i+7][j+6] == "#",
                grid[i+7][j+7] == "#",
                grid[i+7][j+8] == "#",
                
                grid[i+8][j+5] == ".",
                grid[i+8][j+6] == "#",
                grid[i+8][j+7] == "#",
                grid[i+8][j+8] == "#"
            ]) == True:
                print(i+1, j+1)