x = input()
y = len(x)
i = 0
ct = 0
while(i!=y):
    z=x[i]
    if(z == 'A' or z == 'a'):
        ct = ct+1#counter
    i = i+1
print(ct)