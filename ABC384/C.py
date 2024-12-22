from itertools import combinations

def solve(s):
    ans = 0
    if "A" in s:
        ans += a
    if "B" in s:
        ans += b
    if "C" in s:
        ans += c
    if "D" in s:
        ans += d
    if "E" in s:
        ans += e
    return ans

a, b, c, d, e = map(int, input().split())

name = []
result = []
alphabet = "ABCDE"

for i in range(1, len(alphabet)+1):
    for j in combinations(alphabet, i):
        name.append("".join(j))

for i in name:
    score = solve(i)
    result.append((i, score))

result.sort(key=lambda x: (-x[1], x[0]))

for name, _ in result:
    print(name)