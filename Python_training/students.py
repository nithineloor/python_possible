students=['peter','sam','michael','ram']
print(students)
print('Enter your name ')
x=input()
students.append(x)
students.sort()
print(students)
print('Enter your name to be removed from the list')
y=input()
students.remove(y)
print(students)
z = len(students)
print("There are ",z,"students in the classroom")