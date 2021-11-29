file_1 = open('File1.txt','w')
file_1.write('Hi \n')
file_1.write('Hey \n')
file_1.write('How you doing \n')
file_1.write('What is the deal \n')
file_1.write('I like it \n')
file_1.close()

file_2 = open('File2.txt','w')
file_2.write('why \n')
file_2.write('when \n')
file_2.write('who \n')
file_2.write('what \n')
file_2.close()

i = 1
file_1 = open('File1.txt','r')
file_3 = open('Doublefile.txt','w')
for l in file_1:
    file_3.write(l)
    i = i+1
file_3.close()
file_1.close()

k = 1
file_2 = open('File2.txt','r')
file_3 = open('Doublefile.txt','a')
for l in file_2:
    file_3.write(l)
    i = i+1
file_3.close()
file_2.close()