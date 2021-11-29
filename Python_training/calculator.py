#Write a program to do multiplication division,addition and substraction
print('What operation you want')
op = input()
print('Enter a number')
x = int(input())
print('Enter a number')
y = int(input())
z = x*y
i = x/y
su = x-y
ad = x+y
if op == 'Multiplication':
    print('The result is = ',z)
if op == 'Division':
    print('The result is = ',i)
if op == 'Substraction':
    print('The result is = ',su)
if op == 'Addition':
    print('The result is = ',ad)