n, k = map(int, input().split())

a = [1] * (k)
current_sum = sum(a)

for i in range(k, n+1):
    a.append(current_sum % (10**9))
    current_sum = (current_sum + a[-1] - a[-(k+1)]) % (10**9)

print(a[n])
