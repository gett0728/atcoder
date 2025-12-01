from itertools import groupby

def runLengthEncode(S):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

s = input()
rLs = runLengthEncode(s)

print(rLs)

ans = 0

for i in range(len(rLs) - 1):
    num1_str, cnt1 = rLs[i]
    num2_str, cnt2 = rLs[i+1]

    print(num1_str, cnt1, num2_str, cnt2)
    
    num1 = int(num1_str)
    num2 = int(num2_str)

    print(num1, num2)
    
    if num2 == num1 + 1:
        ans += min(cnt1, cnt2)
        
print(ans)
