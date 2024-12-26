n, k = map(int, input().split())
s = list(input())
cnt = 0

for i in range(n - k + 1):
    if s[i:i+k] == list("O" * k):
        cnt += 1
        s[i:i+k] = list("X" * k)

print(cnt)