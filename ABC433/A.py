x, y, z = map(int, input().split())

temp = x - z * y

if temp % (z-1) == 0 and temp // (z-1) >= 0:
    print("Yes")
else:
    print("No")