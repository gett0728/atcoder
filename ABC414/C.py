def is_palindrome(s):
    return s == s[::-1]

def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return str_n[::-1]

a = int(input())
n = int(input())

ans = 0

for i in range(1, 2 * 10**6):
    s = str(i)
    palindrome_odd = int(s + s[:-1][::-1])

    if palindrome_odd > n:
        break
    
    base_n_odd = base_n(palindrome_odd, a)
    if base_n_odd != "-1" and is_palindrome(base_n_odd):
        ans += palindrome_odd
        
    palindrome_even = int(s + s[::-1])
    
    if palindrome_even <= n:
        base_n_even = base_n(palindrome_even, a)
        if base_n_even != "-1" and is_palindrome(base_n_even):
            ans += palindrome_even

print(ans)