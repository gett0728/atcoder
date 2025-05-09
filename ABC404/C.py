n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

if m != n:
    print("No")
    exit()

for i in graph:
    if len(i) != 2:
        print("No")
        exit()

visited = set()
stack = [0]
visited.add(0)

while stack:
    v = stack.pop()
    for u in graph[v]:
        if u not in visited:
            visited.add(u)
            stack.append(u)

if len(visited) == n:
    print("Yes")
else:
    print("No")