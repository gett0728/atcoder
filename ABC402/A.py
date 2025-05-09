s = input()
ans = ""

for i in range(len(s)):
    if s[i].isupper():
        ans += str(s[i])

print(ans)