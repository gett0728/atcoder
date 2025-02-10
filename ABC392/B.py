n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []

if n == m:
    print(0)
    print("")
    exit()

for i in range(1, n+1):
    if not (i in a):
        ans.append(i)

print(len(ans))
print(*ans)