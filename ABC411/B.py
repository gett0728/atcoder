n = int(input())
d = list(map(int, input().split()))

for i in range(n-1):
    ans = []
    temp = 0

    for j in range(i, n-1):
        temp += d[j]
        ans.append(temp)
    
    print(*ans)