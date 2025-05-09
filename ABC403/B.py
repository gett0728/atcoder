t = input().strip()
u = input().strip()
flag = False

for i in range(len(t)-len(u)+1):
    flag2 = True

    for j in range(len(u)):
        if t[i+j] != "?" and t[i+j] != u[j]:
            flag2 = False
            break

    if flag2:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")

