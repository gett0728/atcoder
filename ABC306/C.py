n = int(input())
a = list(map(int, input().split()))
lst = [0] * n
ans = [0] * n

for i in range(n*3):
    if lst[a[i]-1] == 0 or lst[a[i]-1] == 1:
        lst[a[i]-1] += 1
        ans[a[i]-1] = i

ans = sorted([(y, x) for x, y in enumerate(ans)])
print(*[x+1 for y, x in ans])