n = int(input())
flag = False
ans = 0

for _ in range(n):
    s = input()

    if s == "login":
        flag = True
    
    elif s == "logout":
        flag = False

    elif s == "private":
        if not flag:
            ans += 1

print(ans)