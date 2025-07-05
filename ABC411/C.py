n, q = map(int, input().split())
a = list(map(int, input().split()))

color = [0]*n
cnt = 0

for i in range(q):
    idx = a[i] - 1

    black = color[idx] == 1
    left = idx > 0 and color[idx - 1] == 1
    right = idx < n-1 and color[idx + 1] == 1

    if black:
        color[idx] = 0
        if left and right:
            cnt += 1
        elif not left and not right:
            cnt -= 1
    else:
        color[idx] = 1
        if left and right:
            cnt -= 1
        elif not left and not right:
            cnt += 1

    print(cnt)
