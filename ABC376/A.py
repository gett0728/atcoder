n, c = map(int, input().split())
t = list(map(int, input().split()))
cnt = 0

cnt += 1
last = t[0]

for i in range(1, n):
    if t[i] - last >= c:
        cnt += 1
        last = t[i]

print(cnt)