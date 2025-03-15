from collections import deque

q = int(input())

cards = deque([0] * 100)

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        cards.appendleft(query[1])
    elif query[0] == 2:
        print(cards[0])
        cards.popleft()
