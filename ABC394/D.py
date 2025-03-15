s = input()

if len(s) % 2 != 0:
    print("No")
else:
    pairs = {')': '(', ']': '[', '>': '<'}
    stack = []
    
    for i in s:
        if i in {'(', '[', '<'}:
            stack.append(i)
        elif i in {')', ']', '>'}:
            if not stack or stack[-1] != pairs[i]:
                print("No")
                exit()
            stack.pop(-1)
    
    if stack:
        print("No")
    else:
        print("Yes")