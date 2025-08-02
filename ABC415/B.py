s = input()
temp = []

for i in range(len(s)):
    if s[i] == "#":
        temp.append(i+1)

        if len(temp) == 2:
            print(*temp, sep=",")
            temp = []