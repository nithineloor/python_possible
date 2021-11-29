print('type 0 when done')
x = -1
ListOfNum = []
while(x != 0):
    print('Enter a number')
    x = int(input())
    ListOfNum.append(x)
ListOfNum.remove(x)
ListOfNum.sort()
y = len(ListOfNum) - 2
print(ListOfNum)
print('Value of variable y is',y)
print('Element stored in the y position')
print(ListOfNum[y])