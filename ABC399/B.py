n = int(input())
p = list(map(int, input().split()))
score = 100
rank = 1
temp = 0
ans = [0] * n
flag = True

for _ in range(100):
    for i in range(n):
        if p[i] == score:
            ans[i] = rank
            temp += 1
            flag = False
    
    if flag == False:
        rank += temp
        temp = 0
        flag = True
    
    score -= 1

for i in range(n):
    print(ans[i])