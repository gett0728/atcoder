n = int(input())
s = input()

if len(s) % 2 == 0:
    print("No")
    exit()

if len(s) == 1:
    if s == "/":
        print("Yes")
        exit()
    else:
        print("No")
        exit()

t_slash = (n-1) // 2

if s[t_slash] == "/":
    for i in range((n-1)//2):
        if s[i] != "1" or s[t_slash + 1 + i] != "2":
            print("No")
            exit()
else:
    print("No")
    exit()

print("Yes")