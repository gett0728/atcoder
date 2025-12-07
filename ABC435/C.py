n = int(input())
a = list(map(int, input().split()))

limit = a[0]
ans = 0
i = 0
flag = True

while flag:
    if i >= n or i >= limit:
        flag = False
        break

    if i + a[i] > limit:
        limit = i + a[i]

    print(i, a[i], limit, ans)
    ans += 1
    i += 1


print(ans)