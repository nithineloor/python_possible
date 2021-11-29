students = []
print('Enter the number of students')
nos = int(input())#keyboard input number and store into variable nos
while(nos!=0):#While(nos is not equal to zero execute the following lines)
    print('Enter your name')
    x = input()#take the name that you type and save it in variable x
    students.append(x)#append names to the list
    nos = nos-1#reduce one from the value of variable nos
print(students)