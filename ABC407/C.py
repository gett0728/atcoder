from collections import deque

s = input()
s_deque = deque(int(c) for c in s)
cnt = 0
temp = 0

while s_deque:
    back = (s_deque[-1] + temp) % 10

    if back == 0:
        s_deque.pop()
        cnt += 1
    else:
        cnt += back
        temp = (temp - back + 10) % 10
        
print(cnt)