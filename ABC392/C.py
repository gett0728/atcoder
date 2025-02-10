n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pairs = sorted(zip(q, p))
ans = []

for i in range(n):
    ans.append(q[pairs[i][1] - 1])

print(*ans)