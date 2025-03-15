n = int(input())

d = 1
flag = False

while d <= 10**6 and d**3 <= n:
    if n % d == 0:
        a = 3
        b = 3 * d
        c = d**2 - (n//d)
        discriminant = (b**2) - 4*a*c
        root = int(discriminant ** 0.5)

        if discriminant < 0:
            d += 1
            continue

        if root**2 != discriminant:
            d += 1
            continue

        y = (-b + root) // (2*a)

        if (-b + root) % (2*a) == 0 and y > 0:
            x = y + d
            if x > y and x**3 - y**3 == n:
                print(x, y)
                flag = True
                break

    d += 1

if flag == False:
    print(-1)