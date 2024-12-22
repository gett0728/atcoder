n, d = map(int, input().split())
s = input()
cnt = 0

for i in range(n):
    if s[i] == ".":
        cnt += 1

print(cnt + d)
