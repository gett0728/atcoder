n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = set()

for v in range(1, n+1):
    if v not in visited:
        stack = [v]
        visited.add(v)
        nodes, edges = 0, 0
        
        while stack:
            node = stack.pop()
            nodes += 1
            edges += len(graph[node])
            
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    stack.append(neigh)
        
        ans += (edges // 2) - nodes + 1

print(ans)