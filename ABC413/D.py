from collections import Counter
from fractions import Fraction

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 1:
        print("Yes")
        return

    mod_a = sorted([abs(x) for x in a])
    flag = True
    rate = Fraction(mod_a[1], mod_a[0])

    for i in range(n-1):
        if Fraction(mod_a[i+1], mod_a[i]) != rate:
            flag = False
            break
    
    if not flag:
        print("No")
        return

    cnt = Counter(a)
    
    p_p = mod_a
    n_n = [-x for x in mod_a]
    p_n = [mod_a[i] if i % 2 == 0 else -mod_a[i] for i in range(n)]
    n_p = [-mod_a[i] if i % 2 == 0 else mod_a[i] for i in range(n)]

    if cnt == Counter(p_p) or cnt == Counter(n_n) or cnt == Counter(p_n) or cnt == Counter(n_p):
        print("Yes")
        return

    print("No")


t = int(input())

for _ in range(t):
    solve()