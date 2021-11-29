# Write a program to check both exams for marks 30 - 40 then print pass or failed according to the marks.
# take user input 
# take user input again
# if the first exam mark is higher than 30 print pass, else print failed
# if the second exam mark is higher than 40 print pass,else print failed

print('Enter mark of first exam')
x = int(input())
print('Enter mark of second exam')
y = int(input())

if (x >= 40 and y>= 30):
    print('Pass')
else:
    print('Failed')

