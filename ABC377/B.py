pos = [i for i in range(1, 65)]

for i in range(1, 9):
    s = list(input())
    for j in range(8):
        if s[j] == "#":
            for k in range(1, 9):
                dpos = 8 * (i-1) + k
                if dpos in pos:
                    pos.remove(dpos) 
            for k in range(8):
                dpos = 8 * k + j + 1
                if dpos in pos:
                    pos.remove(dpos)

print(len(pos))