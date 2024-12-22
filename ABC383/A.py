n, d = map(int, input().split())
s = list(input())
t = s[:]
cnt = 0

for i in range(1, n+1):
    if cnt == d:
        break
    elif s[-i] == "@":
        t[-i] = "."
        cnt += 1

print("".join(t))