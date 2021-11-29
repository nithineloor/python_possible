x = input()
y = len(x)
rev = ''
while y != 0:
    rev = rev+x[y-1]
    y = y-1
print(rev)
if rev == x:
    print('This is a palindrome')
else:
    print('Not a palindrome')