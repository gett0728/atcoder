n = int(input())
a = list(map(int, input().split()))
temp = 0

for i in range(n):
    if a[i] > temp:
        temp = a[i]
    else:
        print("No")
        exit()

print("Yes")