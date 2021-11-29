#Write a program to save the name of the students
#and assign a random variable as a roll number for each of them.
#after that print the details of each student.
#roll number should contain the first 3 letters of the student's  name.
import random
students = []
roll_numbers = []
print('Enter names of students')
names = ''
while(names != 'end'):
    names = input()
    letters = names[0:3]
    roll_numbers.append(letters)
    students.append(names)
 
k = len(roll_numbers)

for i in range (k):
	rollNum = random.randint(100000,900000)
	rollNum = str(rollNum)
	rollNum = roll_numbers[i]+rollNum
	roll_numbers[i]=rollNum

print('\n')
print('Name','    ', 'Roll Number', '\n')

for i in range (k-1):
	print(students[i],'  ',roll_numbers[i])