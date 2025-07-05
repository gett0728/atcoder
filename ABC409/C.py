n, l = map(int, input().split())
d = list(map(int, input().split()))

if l % 3 != 0:
    print(0)
    exit()

temp = 0
cnt = [0] * l

for i in range(n):
    if i != 0:
        temp += d[i-1]
    
    temp %= l
    cnt[temp] += 1

ans = 0

for i in range(l//3):
    p1 = i
    p2 = i + l//3
    p3 = i + (2*l)//3

    ans += cnt[p1] * cnt[p2] * cnt[p3]

print(ans)