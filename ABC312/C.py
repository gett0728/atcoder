from bisect import *

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

def check(x):
    return bisect_right(a, x) >= m - bisect_left(b, x)

ng = 0
ok = 10**9 + 1

while abs(ok - ng) > 1:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
