import random
file_1 = open('random_line.txt','r')
l=0
for i in file_1:
    l = l+1
x = random.randint(0,l)
print(x)
file_1.close()
file_1 = open('random_line.txt','r')
l = 0
for i in file_1:
    if l == x:
        print(i)
    l = l+1