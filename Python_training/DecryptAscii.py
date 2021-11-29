file_1 = open('Jim.txt','r')
words = []
for l in file_1:
    words = words + l.split(',')
print(words)
file_1.close()
file_1 = open('Jim_dec.txt','w')
for i in words:
    x = int(i)
    x = x-5
    if x == 32:
        file_1 = open('Jim_dec.txt','a')
        file_1.write(' ')
    else:
        x = chr(x)
        file_1 = open('Jim_dec.txt','a')
        file_1.write(x)
file_1.close()