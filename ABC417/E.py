def dfs(v):
        path.append(v)
        visited[v] = True

        if v == y:
            print(*path)
            return

        for neigh in graph[v]:
            if not visited[neigh] and dfs(neigh):
                return True

        path.pop()
        return False


def solve():
    global graph, path, visited
    global n, m, x, y

    n, m, x, y = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        graph[i].sort()

    path = []
    visited = [False] * (n+1)

    dfs(x)


t = int(input())
for _ in range(t):
    solve()