n = int(input())
lst = []
ans = set()

for i in range(n):
    s = input()
    lst.append(s)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            ans.add(lst[i] + lst[j])

print(len(ans))