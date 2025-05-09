s = input()
lst = set()

for i in range(len(s)):
    lst.add(ord(s[i]))

for i in range(97, 123):
    if not(i in lst):
        print(chr(i))
        exit()

