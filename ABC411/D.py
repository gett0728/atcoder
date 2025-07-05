n, q = map(int, input().split())
op = []
p = []
s = []

for _ in range(q):
    query = input().split()
    op.append(int(query[0]))
    p.append(int(query[1]))

    if int(query[0]) == 2:
        str_data = query[2][::-1]
        s.append(str_data)
    else:
        s.append("")
    
    print(str_data)

ans = ""
i = 0

for t in reversed(range(q)):
    if op[t] == 1:
        if i == p[t]:
            i = 0

    elif op[t] == 2:
        if i == p[t]:
            ans += s[t]
            
    elif op[t] == 3:
        if i == 0:
            i = p[t]

print(ans[::-1])
