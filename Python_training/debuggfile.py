# write a program to store the names of students into a list. 
# The program should stop when the user type "End" as an input.
x = ''
x = input()# take keyboard input and store to variable
students = []#Students is an empty list
while(x != 'end'):# While x is not equal to End  loop the following.
    students.append(x)# add user input name to list
print(students)# print the list