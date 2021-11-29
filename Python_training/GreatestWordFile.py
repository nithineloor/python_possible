file_1 = open('largest_word.txt','r')
words = []



for l in file_1:
    words = words+l.split(" ")

length = len(words[0])

longest = words[0]

  
for i in words:
	if(len(i) > length):
  
		length = len(i)
		longest = i
  
print(longest)