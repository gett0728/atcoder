n = int(input())
a = list(map(int, input().split()))
ans = 0

for l in range(n):
    for r in range(l+1, n):
        sub = a[l:r+1]
        s = sum(sub)

        ok = True
        for x in sub:
            if s % x == 0:
                ok = False
                break
        
        if ok:
            ans += 1

print(ans)