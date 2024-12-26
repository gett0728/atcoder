n = int(input())
s = input()
cnt = 0

for i in range(2, n):
    if s[i - 2] == "#" and s[i - 1] =="." and s[i] == "#":
        cnt += 1

print(cnt)