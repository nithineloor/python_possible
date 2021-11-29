#Write a program to do multiplication division and substraction
print('What operation you want(Multiplication,Division,Substraction,Addition)')
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
elif op == 'Division':
    print('The result is = ',i)

elif op == 'Substraction':
    print('The result is = ',su)

elif op == 'Addition':
    print('The result is = ',ad)
else:
    print('Oops I think yo misspelled right there')