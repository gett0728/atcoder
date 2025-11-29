n, m = map(int, input().split())
ans = [[0, 0] for _ in range(m)]

for i in range(n):
    a, b = map(int, input().split())

    ans[a-1][0] += b
    ans[a-1][1] += 1

for i in range(m):
    print(ans[i][0] / ans[i][1])