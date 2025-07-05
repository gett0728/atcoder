n, q = map(int, input().split())
a = [i for i in range(1, n+1)]
offset = 0

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        p = query[1] - 1
        x = query[2]
        a[(p + offset) % n] = x

    elif query[0] == 2:
        p = query[1] - 1
        print(a[(p + offset) % n])

    elif query[0] == 3:
        k = query[1]
        offset = (offset + k) % n
