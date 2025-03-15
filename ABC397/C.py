n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n
ans = 0
lst = set()

for i in range(n):
    lst.add(a[i])
    left[i] = len(lst)

lst.clear()

for i in range(n-1, -1, -1):
    lst.add(a[i])
    right[i] = len(lst)

for i in range(n-1):
    ans = max(ans, left[i] + right[i+1])

print(ans)
