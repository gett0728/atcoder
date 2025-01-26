import bisect

n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    mid = bisect.bisect_right(a, a[-i]/2)
    ans += mid

print(ans)
