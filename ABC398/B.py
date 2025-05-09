a = list(map(int, input().split()))

cards = [0]*13

for i in a:
    cards[i-1] += 1

for i in range(len(cards)):
    if cards[i] == 2:
        for j in range(i+1, len(cards)):
            if cards[j] > 2:
                print("Yes")
                exit()
    
    if cards[i] > 2:
        for j in range(i+1, len(cards)):
            if cards[j] >= 2:
                print("Yes")
                exit()

print("No")