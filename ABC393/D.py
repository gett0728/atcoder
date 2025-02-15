n = int(input())
s = input()
ans = 0

one_index = [i for i, c in enumerate(s) if c == "1"]

center = one_index[len(one_index) // 2]
target = [(center - (len(one_index) // 2) + i) for i in range(len(one_index))]

for i in range(len(one_index)):
    ans += abs(one_index[i] - target[i])

print(ans)