n, m, q = map(int, input().split())

lst = [set() for _ in range(n)]
ok = [False] * n

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        lst[query[1]-1].add(query[2])

    elif query[0] == 2:
        ok[query[1]-1] = True

    elif query[0] == 3:
        if ok[query[1]-1] or query[2] in lst[query[1]-1]:
            print("Yes")
        else:
            print("No")
