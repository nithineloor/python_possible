#Make for loop range
for i in range(1000,5000):
#Convert to string with another var
    s=str(i)
    l=0
    for j in s:
        j=int(j)
        k=j%2
        if k!=0:
            l=1
    if l==0:
        print(s)