from math import factorial as fac

x = int(input())
ans_lst = [fac(i) for i in range(1, 21)]

for i in range(20):
    if x == ans_lst[i]:
        print(i+1)