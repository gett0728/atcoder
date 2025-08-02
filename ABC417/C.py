from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

cnt = defaultdict(int)
ans = 0

for j in range(n):
    temp = j - a[j]
    ans += cnt.get(temp, 0)
    cnt[j + a[j]] += 1

print(ans)
