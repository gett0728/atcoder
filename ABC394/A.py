s = input()
temp = 0

for i in range(len(s)):
    if s[i] == "2":
        temp += 1

print(*([2] * temp), sep="")