n, d = map(int, input().split())
s = [input().strip() for _ in range(n)]

ans, cur = 0, 0

for j in range(d):
    flag = all(s[i][j] == "o" for i in range(n))

    if flag:
        cur += 1
    else:
        cur = 0
    
    ans = max(ans, cur)

print(ans)