def solve():
    n, h = map(int, input().split())

    goals = []
    for _ in range(n):
        t, l, u = map(int, input().split())
        goals.append((t, l, u))

    temp = 0
    high = h
    low = h

    for t, l, u in goals:
        dt = t - temp

        low = max(0, low - dt)
        high = high + dt

        low = max(low, l)
        high = min(high, u)

        if high <= 0 or low > high:
            print("No")
            return

        temp = t

    print("Yes")


t = int(input())
for _ in range(t):
    solve()