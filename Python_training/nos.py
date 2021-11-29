# write a program to store the names of students into a list. 
# The program should stop when the user type "End" as an input.
x = ''
students = []#Students is an empty list
while(x != 'end'):# While x is not equal to End  loop the following.
    print('Enter student name')
    x = input()# take keyboard input and store to variable
    students.append(x)# add user input name to list
students.remove('end')
print(students)# print the list