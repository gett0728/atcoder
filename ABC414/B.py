n = int(input())
s = ""
temp = 0

for i in range(n):
    c, l = input().split()
    l = int(l)
    temp += l
    if temp > 100:
        print("Too Long")
        exit()

    for j in range(l):
        s += str(c)
        
print(s)