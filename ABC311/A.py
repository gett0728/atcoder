n = int(input())
s = input()
flag_a = False
flag_b = False
flag_c = False

for i in range(n):
    if s[i] == "A":
        flag_a = True
    elif s[i] == "B":
        flag_b = True
    elif s[i] == "C":
        flag_c = True
    
    if flag_a and flag_b and flag_c:
        print(i+1)
        exit()