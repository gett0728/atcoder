from collections import Counter

a, b, c, d = map(int, input().split())
card = [0 for _ in range(13)]

for i in range(1, 14):
    if a == i:
        card[i-1] += 1
    if b == i:
        card[i-1] += 1
    if c == i:
        card[i-1] += 1
    if d == i:
        card[i-1] += 1
    
counts = Counter(card)

if counts[2] == 2 or (counts[1] == 1 and counts[3] == 1):
    print("Yes")
else:
    print("No")