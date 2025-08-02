s = input()
t = list(s)

o = -2
sharp = -1

for i in range(len(s)):
    if s[i] == "#":
        t[i] = "#"
        sharp = i

    else:
        if o < sharp:
            t[i] = "o"
            o = i
        else:
            t[i] = "."

print("".join(t))
