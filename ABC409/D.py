def solve():
    n = int(input())
    s = input()
    l = -1

    for i in range(1, n):
        if s[i-1] > s[i]:
            l = i-1
            break
    
    if l == -1:
        print(s)
        return
    
    r = n

    for i in range(l+1, n):
        if s[l] < s[i]:
            r = i
            break
    
    print(s[:l] + s[l+1:r] + s[l] + s[r:])

t = int(input())

for _ in range(t):
    solve()

