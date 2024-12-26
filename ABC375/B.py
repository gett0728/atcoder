import math

n = int(input())
x_temp, y_temp = 0, 0
sum_cost = 0

for _ in range(n):
    x, y = map(int, input().split())
    sum_cost += math.sqrt((x_temp - x) ** 2 + (y_temp - y) ** 2)
    x_temp, y_temp = x, y

sum_cost += math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

print(sum_cost)