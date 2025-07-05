n = int(input())
a = list(map(int, input().split()))

left = 0
right = n+1

while right - left > 1:
    mid = (left + right) // 2
    cnt = 0

    for i in range(n):
        if a[i] >= mid:
            cnt += 1

    if cnt >= mid:
        left = mid
    else:
        right = mid

print(left)


# n = int(input())
# a = list(map(int, input().split()))

# for i in range(n, -1, -1):
#     cnt = 0

#     for char in a:
#         if char >= i:
#             cnt += 1
    
#     if cnt >= i:
#         print(i)
#         exit()