from sortedcontainers import SortedList

n, m, k = map(int, input().split())
h = list(map(int, input().split()))
b = SortedList(map(int, input().split()))

h.sort()

limit = 0

for i in range(n):
    ans = b.bisect_left(h[i])
    
    if ans < len(b):
        b.pop(ans)
        limit += 1
        
        if limit >= k:
            print("Yes")
            exit()

print("No")