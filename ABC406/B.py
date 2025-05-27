n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 1

for i in range(n):
    ans *= a[i]

    if len(str(ans)) > k:
        ans = 1

print(ans)