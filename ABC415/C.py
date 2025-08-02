def solve():
    n = int(input())
    s = input()

    is_safe = [False] * (1 << n)

    for i in range(len(s)):
        if s[i] == "0":
            is_safe[i+1] = True

    dp = [False] * (1 << n)
    dp[0] = True

    for mask in range(1, 1 << n):
        if not is_safe[mask]:
            continue

        for i in range(n):
            if (mask >> i) & 1:
                prev_mask = mask ^ (1 << i)

                if dp[prev_mask]:
                    dp[mask] = True
                    break
    if dp[(1 << n) - 1]:
        print("Yes")
    else:
        print("No")

t = int(input())

for _ in range(t):
    solve()