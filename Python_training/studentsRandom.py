#Write a program to save the name of the students !Done
#and assign a random variable as a roll number for each of them.!Done
#after that print the details of each student.
#roll number should contain the first 3 letters of the student's  name.
import random
students = []
print('Enter names of students')
names = ''
letterRollNum = []

while(names != 'end'):
    names = input()
    x = names[0:3]
    letterRollNum.append(x)
    students.append(names)

roll_numbers = []

while(len(roll_numbers) != len(students)):
    rollNum = random.randint(1000000,10000000)
    rollNum = str(rollNum)
    roll_numbers.append(rollNum)

FullRoll = []
while(len(FullRoll) != len(students)):
    y = letterRollNum[0] + roll_numbers[0]
    FullRoll.append(y)
    letterRollNum.remove(letterRollNum[0])
    roll_numbers.remove(roll_numbers[0])

print('Name','       ','Roll Number')

while(len(students) != 0):
    print(students[0],'       ',FullRoll[0])
    students.remove(students[0])
    FullRoll.remove(FullRoll[0])