n, q = map(int, input().split())
x = list(map(int, input().split()))
box = [0] * n
ans = []

for i in range(q):
    if x[i] >= 1:
        ans.append(x[i])
        box[x[i]-1] += 1
    elif x[i] == 0:
        _min = min(box)
        for j in range(n):
            if box[j] == _min:
                ans.append(j+1)
                box[j] += 1
                break

print(*ans)