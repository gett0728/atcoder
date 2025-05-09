q = int(input())
lst = []

for i in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        lst.append(query[1])
    
    elif query[0] == 2:
        print(lst[0])
        lst.pop(0)
