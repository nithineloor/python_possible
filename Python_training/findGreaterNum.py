# Write a program to find the greatest number.

print('Enter a number')
x = int(input())
print('Enter another number')
y = int(input())

if x > y:
    print(x,"is greater than",y)
elif x == y:
    print(x,"the equal to",y)
else:
    print(x,"is smaller than",y)