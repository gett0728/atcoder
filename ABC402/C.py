from collections import defaultdict

n, m = map(int, input().split())
foods = []

lst = defaultdict(list)
weak = [0] * m

for i in range(m):
    food = list(map(int, input().split()))
    ingredients = food[1:]
    foods.append(ingredients)

    for j in ingredients:
        lst[j-1].append(i)
        weak[i] += 1

B = list(map(int, input().split()))

ok = 0
ans = []

for i in B:
    i -= 1

    for dish in lst[i]:
        weak[dish] -= 1

        if weak[dish] == 0:
            ok += 1

    ans.append(ok)

print(*ans, sep="\n")