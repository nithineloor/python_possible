import random
print('Enter your mobile number')
x = int(input())
y = random.randint(1000000000,10000000000)
while y != x:
    y = random.randint(1000000000,10000000000)
print(y)
if x >=y:
    i = x - y
else:
    i = y - x
print('The value difference between your mobile number and the generated number is',i) 