x = int(input())
n = int(input())
w = list(map(int, input().split()))
q = int(input())

is_equip = [False] * n

for i in range(q):
    p = int(input())

    is_equip[p-1] = not is_equip[p-1]

    ans = []
    for j in range(n):
        ans.append(w[j] if is_equip[j] else 0)
    
    print(x + sum(ans))
