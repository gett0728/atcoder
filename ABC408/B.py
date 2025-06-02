n = int(input())
a = list(map(int, input().split()))

ans = set(a)
ans = sorted(list(ans))

print(len(ans))
print(*ans)