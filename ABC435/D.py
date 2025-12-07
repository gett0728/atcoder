n, m = map(int, input().split())
graph = [100] + [[] for _ in range(n)]
graph_color = [100] + [0 for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    v = query[1]

    if query[0] == 1:
        if graph_color[v] == 0:
            graph_color[v] = 1
            stack = [v]

            while stack:
                curr = stack.pop()
                for neigh in graph[curr]:
                    if graph_color[neigh] == 0:
                        graph_color[neigh] = 1
                        stack.append(neigh)

    elif query[0] == 2:
        if graph_color[v] == 1:
            print("Yes")
        else:
            print("No")