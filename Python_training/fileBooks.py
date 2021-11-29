name = open('book.docx','w')
name.close()
g = 5
while(g != 0):
    g = g-1

    print('What is your name')
    x = input()
    print('What is your favorite book')
    y = input()

    name = open('book.docx','a')
    name.write(x+'\n')
    name.write(y+'\n')
    name.close()