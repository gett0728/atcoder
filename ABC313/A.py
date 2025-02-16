n = int(input())
p = list(map(int, input().split()))

if len(p) == 1:
    print(0)
    exit()

if p[0] > max(p[1:n]):
    print(0)
else:
    print(abs(max(p[1:n]) - p[0]) + 1)
