n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0

for i in range(1, m+1):
    if not (i in a):
        print(0)
        exit()

while True:
    a.pop(-1)
    ans += 1
    for i in range(1, m+1):
        if not (i in a):
            print(ans)
            exit()