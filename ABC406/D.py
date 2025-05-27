h, w, n = map(int, input().split())

row = {}
col = {}

for _ in range(n):
    x, y = map(int, input().split())
    row.setdefault(x, set()).add((x, y))
    col.setdefault(y, set()).add((x, y))

q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        x = query[1]
        remove = row.get(x, set())
    else:
        y = query[1]
        remove = col.get(y, set())

    cnt = len(remove)
    print(cnt)

    for x, y in remove.copy():
        row.get(x, set()).discard((x, y))
        col.get(y, set()).discard((x, y))
