a = list(map(int, input().split()))
color_count = {}
cnt = 0

for color in a:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

for count in color_count.values():
    cnt += count // 2

print(cnt)