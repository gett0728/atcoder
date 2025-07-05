from collections import deque

q = int(input())
a = deque()

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        x = query[2]
        a.append([x, c])
    
    elif query[0] == 2 :
        k = query[1]
        ans = 0
        
        while k > 0:
            val, cnt = a[0]
            if k >= cnt:
                ans += val * cnt
                a.popleft()
                k -= cnt
            else:
                ans += val * k
                a[0][1] -= k
                k = 0
                
        print(ans)