import itertools

n, k, x = map(int, input().split())
lst = [input() for _ in range(n)]

ans = []

for indices in itertools.product(range(n), repeat=k):
    s = "".join(lst[i] for i in indices)
    ans.append(s)

ans.sort()

print(ans[x-1])