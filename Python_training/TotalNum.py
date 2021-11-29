#Write a program to  find the numbers between 1000 and 5000 such that every digit in that number is an even number
for i in range(1000,5000):
    x = str(i)
    l=0
    for y in x:
        y=int(y)
        if y == 0:
            l=1
        f=y%2
        if f!=0:
            l=1
    if l==0:
        print(x)