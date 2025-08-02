def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    k = 0
    i = 0
    j = n - 1

    while i < n and j >= 0:
        if a[i] + b[j] >= m:
            k += 1
            i += 1
            j -= 1 
        else:
            i += 1

    total_sum = sum(a) + sum(b)
    ans = total_sum - k * m

    print(ans)

t = int(input())

for _ in range(t):
    solve()