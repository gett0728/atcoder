n, m = map(int, input().split())

loop = 0
edge = {}

for _ in range(m):
    u, v = map(int, input().split())
    if u == v:
        loop += 1
    else:
        temp = tuple(sorted((u, v)))
        edge[temp] = edge.get(temp, 0) + 1

edgesum = sum(count - 1 for count in edge.values())

print(loop + edgesum)