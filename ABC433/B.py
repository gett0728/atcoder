n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    frag = False

    for j in range(i-1, -1, -1):
        if a[j] > a[i]:
            print(j+1)
            frag = True
            break
    
    if not frag:
        print(-1)