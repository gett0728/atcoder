k = int(input())
s = list(input())
t = list(input())

cnt = 0

def sist():
    if s == t:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if s == t:
    print("Yes")
    exit()

if abs(len(s) - len(t)) >= 2:
    print("No")
    exit()

if len(s) == len(t):
    for i in range(len(s)):
        if s[i] == t[i]:
            cnt += 1
    if cnt == len(s)-1:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if len(s) < len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            s.insert(i, t[i])
            sist()
    s.insert(i+1, t[-1])
    sist()
else:
    for i in range(len(t)):
        if s[i] != t[i]:
            t.insert(i, s[i])
            sist()
    t.insert(i+1, s[-1])
    sist()