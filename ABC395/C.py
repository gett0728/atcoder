n = int(input())
a = list(map(int, input().split()))
index_map = {}
_min = float('inf')

for j in range(n):
    if a[j] in index_map:
        _min = min(_min, j - index_map[a[j]] + 1)
    index_map[a[j]] = j

if _min != float("inf"):
    print(_min)
else:
    print(-1)
