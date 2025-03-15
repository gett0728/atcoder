n = int(input())
lst = []

for i in range(n):
    s = input()
    lst.append(s)

ans = sorted(lst, key=len)

print(*ans, sep="")