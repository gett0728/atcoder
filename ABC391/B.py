n, m = map(int, input().split())

grid_s = []
grid_t = []

for i in range(n):
    s = list(input())
    grid_s.append(s)

for i in range(m):
    t = list(input())
    grid_t.append(t)

for i in range(n-m+1):
    for j in range(n-m+1):
        flag = True
        for x in range(m):
            for y in range(m):
                if grid_s[i+x][j+y] != grid_t[x][y]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(i+1, j+1)
            exit()