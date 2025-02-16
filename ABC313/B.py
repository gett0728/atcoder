n, m = map(int, input().split())
s = set(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    s.discard(b)

print(-1 if len(s) != 1 else s.pop())