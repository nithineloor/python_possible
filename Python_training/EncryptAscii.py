file_1 = open("Hi.txt",'r')
words = []
Ascii_word =  []
word = []
word2 = []
space = []
sentence = []
encrypt = []
word_space = []

for l in file_1:
    words = words+l.split(" ")
for s in words:
    word_space.append(s)
    word_space.append(" ")
for o in word_space:
    for i in o:
        c = ord(i)
        Ascii_word.append(c)
for n in Ascii_word:
    n = n+5
    encrypt.append(n)
print(encrypt)

# sentence.append(word)
# sentence.append(space)
# sentence.append(word2)

# for j in sentence:
#     word.append(n)
#     space.append(" ")
#     word2.append(n)

# # print(sentence)

# file_2 = open('Jim.txt','w')
# for b in encrypt:
#     for v in b:
#         word = str(v)
#         file_2 = open('Jim.txt','a')
#         file_2.write(word)
#         file_2.write(',')