n, m = map(int, input().split())
canon = []
diff = [0] * (n+2)
wall = [0] * (n+1)

for i in range(m):
    l, r = map(int, input().split())
    canon.append([l, r])

for l, r in canon:
    diff[l] += 1
    diff[r+1] -= 1

for i in range(1, n+1):
    wall[i] = wall[i-1] + diff[i]

print(min(wall[1:]))