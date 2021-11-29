file_1 = open('My_file.txt','w')
file_1.write('Hello this is my file \n')
file_1.write('Ok then Bye \n')
x = input
file_1.write(x)
file_1.close()
file_1 = open('My_file.txt','r')
i = 1
for l in file_1:
	print('This is line', i)
	print(l)
	i = i+1
file_1.close()