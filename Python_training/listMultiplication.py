listnum = []
x = 1
p = 1
while(x != 0):
    print('Enter a value')
    x = int(input())
    listnum.append(x)
    if x != 0:
        p = x*p
z = len(listnum)- 1
listnum.remove(listnum[z])
print(listnum)
print(p)