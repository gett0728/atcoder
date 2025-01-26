n, d = map(int, input().split())

snake_t = []
snake_l = []

for i in range(n):
    t, l = map(int, input().split())
    snake_t.append(t)
    snake_l.append(l)

for i in range(1, d+1):
    max_ = 0
    for j in range(n):
        max_ = max(max_, snake_t[j] * (snake_l[j] + i))
    print(max_)
