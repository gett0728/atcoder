s = list(input())

cnt = 0
i = 0

while i < len(s):
    if s[i] == "0":
        if i+1 < len(s) and s[i+1] == "0":
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    else:
        cnt += 1
        i += 1

print(cnt)