#write a program to find the book name from the library
#user may input the book name or author name
books = {'JK Rolling' : 'harry potter' , 'Dave Pilkey' : 'dogman','R.L.Stine'  : 'Goosebumps','harry Potter' : 'harry potter','dogMan' : 'dogman','goosebumps' : 'Goosebumps'}
print('What book do you want')
x = input()
x = x.lower()
if x == 'jk rolling':
    print(books['JK Rolling'])
elif x == 'harry potter':
    print(books['harry Potter'])
elif x == 'dave pilkey':
    print(books['Dave Pilkey'])
elif x == 'dog man':
    print(books['dogMan'])
elif x == 'goosebumps':
    print(books['goosebumps'])
elif x == 'rl stine':
    print(books['R.L.Stine'])
else:
    print('This book is unavailable at the moment please come again next time')