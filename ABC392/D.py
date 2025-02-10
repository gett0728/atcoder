from collections import Counter
from itertools import combinations
import sys

input = sys.stdin.read
data = input().strip().split('\n')

n = int(data[0])
dice = []

for i in range(1, n+1):
    line = list(map(int, data[i].split()))
    faces = line[1:]
    dice.append(faces)

ans = 0

for dice1, dice2 in combinations(dice, 2):
    count1 = Counter(dice1)
    count2 = Counter(dice2)
    common_faces = set(dice1) & set(dice2)
    
    probability = 0
    for face in common_faces:
        probability += (count1[face] / len(dice1)) * (count2[face] / len(dice2))
    
    ans = max(ans, probability)

print(ans)