s = input()
t = input()
lst = []

for i in range(1, len(s)):
    if s[i].isupper():
        lst.append(s[i-1])

for i in range(len(lst)):
    if lst[i] in t:
        pass
    else:
        print("No")
        exit()

print("Yes")