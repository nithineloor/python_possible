x = -1
flag = 1
num = []
while(x != 0):
    print('Enter a value')
    x = int(input())
    if x < 0:
        flag = 0 #setting a flag to check the occurence of a negative number
if flag == 0: #checking the flag
    print('Your list contains a negative number')
else:
    print('Your list only contains positive numbers')