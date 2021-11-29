x = input()
y = len(x)
rev = ''
for i in range (y):
    rev = rev+x[y-1]
    y=y-1
print(rev)