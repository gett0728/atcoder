s = input()
temp = 0
li = []

for i in range(1, len(s)):
    if s[i] == "|":
        li.append(i - temp - 1)
        temp = i

print(*li)
