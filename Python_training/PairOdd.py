#Write a program to Multiply pair numbers by 2 else multiply by 3
#Take user input
#If user input = pair number multiply by 2 else multiply by 3
#Print this is a even/odd number
#print the results
print('This programme will multiply your number into 2 or 3 depending whether its a even number or not')
print('Enter a number')
x = int(input())
y = x%2
if y == 0:
    print('This is a even number')
    print(x*2)
else:
    print('this is an odd number')
    print(x*3)