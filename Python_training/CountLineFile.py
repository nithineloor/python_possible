file_1 = open('line_count.txt','r')
i = 1
for l in file_1:
    i = i+1
print(i-1)
file_1.close()