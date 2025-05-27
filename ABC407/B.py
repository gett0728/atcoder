x, y = map(int, input().split())

temp = 0

for i in range(1, 7):
    for j in range(1, 7):
        if i+j >= x or abs(i-j) >= y:
            temp += 1

print(temp / 36)
