n = int(input())
a = list(map(int, input().split()))

count = {}
max_value = -1
max_index = -1

for i in range(n):
    count[a[i]] = count.get(a[i], 0) + 1

for i in range(n):
    if count[a[i]] == 1:
        if a[i] > max_value:
            max_value = a[i]
            max_index = i + 1

print(max_index)