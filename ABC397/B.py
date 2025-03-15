import re

s = input()
s_ = re.findall(r"i+|o+", s)
ans = 0

for i in range(len(s_)):
    if len(s_[i]) > 1:
        ans += len(s_[i]) - 1

if s[0] == "o":
    ans += 1

if s[-1] == "i":
    ans += 1

print(ans)