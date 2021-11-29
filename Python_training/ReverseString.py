x = input()
y = len(x)
rev = ''
while y != 0:
    rev = rev+x[y-1]
    y = y-1
print(rev)