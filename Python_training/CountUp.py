import random
x = int(input())
y = 0
count = 0
while count != x:
    count = random.randint(0,x+100)
    y = y+1
print(y)