n = int(input())
a = list(map(int, input().split()))
ans = 0

s = sum(a)

for i in range(n-1):
    s -= a[i]
    ans += a[i] * s

print(ans)