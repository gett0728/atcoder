def f(s):
    ones = [0] * (n+1)

    for i in range(n):
        ones[i+1] = ones[i] + int(s[i])

    total = ones[n]
    lst = [0] * (n+1)

    for i in range(n+1):
        lst[i] = i - 2 * ones[i]

    lst_r = [0] * (n+1)
    lst_r[n] = lst[n]

    for i in range(n-1, -1, -1):
        lst_r[i] = min(lst_r[i+1], lst[i])

    min_diff = 0

    for i in range(n+1):
        diff = lst_r[i] - lst[i]
        min_diff = min(diff, min_diff)

    return total + min_diff

t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    print(f(s))