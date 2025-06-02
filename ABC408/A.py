n, s = map(int, input().split())
t = list(map(int, input().split()))
flag = True

if t[0] >= s + 0.5:
    print("No")
    exit()

for i in range(n-1):
    if abs(t[i+1] - t[i]) >= s + 0.5:
        flag = False

if flag:
    print("Yes")
else:
    print("No")