import re

s = input()

ans = re.split(r'(?<=WA)(?=.)|(?<=[^W])(?=WA)|(?<=[W])(?=[^A])', s)

for i in range(len(ans)):
    if len(ans[i]) <= 1:
        continue
    if ans[i][-1] == "A" and ans[i][-2] == "W":
        ans[i] = "A" + "C"*(len(ans[i])-1)

print(*ans, sep="")