n = int(input())
inputs = []

for _ in range(n):
    w, h, b = map(int, input().split())
    inputs.append((w, h, b))

total_w = sum(w for w, h, b in inputs)

dp = [-1] * (total_w + 1)
dp[0] = 0

for w, h, b in inputs:
    new_dp = dp[:]

    for head_w in range(total_w + 1):
        if dp[head_w] == -1:
            continue

        if head_w + w <= total_w:
            new_dp[head_w + w] = max(new_dp[head_w + w], dp[head_w] + h)

        new_dp[head_w] = max(new_dp[head_w], dp[head_w] + b)

    dp = new_dp

ans = 0
for head_w in range(total_w + 1):
    body_w = total_w - head_w

    if head_w <= body_w and dp[head_w] != -1:
        ans = max(ans, dp[head_w])

print(ans)