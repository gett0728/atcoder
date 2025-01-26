a1, a2, a3, a4, a5 = map(int, input().split())

lst = [a1, a2, a3, a4, a5]
lst_ans = lst[:]
flag = True

if lst_ans == [1, 2, 3, 4, 5]:
    print("No")
    exit()

for i in range(4):
    if lst[i] == i+1 and flag:
        continue
    elif lst[i] != i+1 and flag:
        lst_ans[i] = lst[i+1]
        lst_ans[i+1] = lst[i]
        flag = False

if lst_ans == [1, 2, 3, 4, 5]:
    print("Yes")
else:
    print("No")