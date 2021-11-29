file_1 = open('file_open.docx','w')
file_1.write("I am writing this to the file \n") 
file_1.write("This is the next sentence ::) \n")
file_1.close()
# Appending new line
file_1 = open('file_open.docx','a') 
file_1.write("This is the appended line:")
file_1.close()
#Reading entire file
file_1=open('file_open.docx','r')
print (file_1.read())
file_1.close()
#Reading the first line
file_1 = open('file_open.docx','r')
k= file_1.readline()
print(k)
j= file_1.readline()
print(j)
file_1.close()