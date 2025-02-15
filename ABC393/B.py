s = input()
ans = 0

for i in range(len(s)):
    if s[i] != "A":
        continue

    for j in range(i+1, len(s)):
        if s[j] != "B":
            continue

        temp = j - i
        k = j + temp

        if k < len(s) and s[k] == "C":
            ans += 1

print(ans)
