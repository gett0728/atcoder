n = int(input())
MOD = 998244353
ans = 0

inv = pow(2, MOD-2, MOD)

i = 2
while i <= n:
    q = n // i
    r = n // q
    num = r - i + 1
    temp = n - q + 1

    _sum = ((temp % MOD) * (num % MOD)) % MOD
    sum_b = ((((i + r) % MOD) * (num % MOD)) % MOD) * inv

    range_sum = (_sum - sum_b + MOD) % MOD
    ans = (ans + range_sum) % MOD

    i = r + 1

print(ans)