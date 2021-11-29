print("Enter a word to check if it's a palindrome")
x = input()
u = ''
for i in x:
    u = i+u
if u == x:
    print("This is a palindrome")
else:
    print("This is not a palindrome")