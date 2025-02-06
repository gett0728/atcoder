h, w, x, y = map(int, input().split())
x -= 1
y -= 1
grid = []
for i in range(h):
    s = list(input())
    grid.append(s)
t = input()
cnt = 0

for i in range(len(t)):
    if t[i] == "U" and grid[x-1][y] != "#":
        x -= 1
    if t[i] == "D" and grid[x+1][y] != "#":
        x += 1
    if t[i] == "L" and grid[x][y-1] != "#":
        y -= 1
    if t[i] == "R" and grid[x][y+1] != "#":
        y += 1
    
    if grid[x][y] == "@":
        cnt += 1
        grid[x][y] = "."

print(x+1, y+1, cnt)