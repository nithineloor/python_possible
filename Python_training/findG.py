#Write a program to find whether there is the character "G"
#take user input 
#find lenght of user input
#use for loop to iterate between each character 
# if the string contains a G then print I found G
print('Enter a Noun')
name = input()
for i in range(len(name)):
    if name[i] == 'g':
        print('I found a G')
    else:
        print("I didn't find a G")