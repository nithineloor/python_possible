#Write a program to print all odd numbers between 1 and 1000
#tell user what program will do
#make a for loop to print all numbers 1 to 1000
#check each number before printing if number is odd or not
#print the number that is odd
# don't print if it's even
print('odd numbers between 1 and 1000')
for i in range(1,1000):
    x = i%2
    if x == 1:
        print(i)