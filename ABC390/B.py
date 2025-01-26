n = int(input())
a = list(map(int, input().split()))

Gratio = a[1] / a[0]

for i in range(n-1):
    if a[i+1] != Gratio * a[i]:
        print("No")
        exit()

print("Yes")