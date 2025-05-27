a, b, c, d = map(int, input().split())

deadline = a * 60 + b
submit = c * 60 + d

if submit <= deadline:
    print("Yes")
else:
    print("No")
