Jimmy=[26,26000]
Ron=[24,26000]
Neil=[27,32000]
Alex=[26,32000]
Kate=[30,60000]
print("Who's details do you want, Jimmy,Ron,Neil,Alex or Kate")
x = input()
if x=='Jimmy'or'jimmy':
    print(Jimmy)
elif x=='Ron'or'ron':
    print(Ron)
elif x=='Neil'or'neil':
    print(Neil)
elif x=='Alex'or'alex':
    print(Alex)
elif x=='Kate'or'kate':
    print(Kate)
else:
    print('That is not an employee')
print("Who's salary do you want to increase")
y =input()
if x=='Jimmy'or'jimmy':
    Jimmy[1] = Jimmy[1]+1000
    print(Jimmy)
elif x=='Ron'or'ron':
    Ron[1] = Ron[1]+1000
    print(Ron)
elif x=='Neil'or'neil':
    Neil = Neil[1]+1000
    print(Neil)
elif x=='Alex'or'alex':
    Alex = Alex[1]+1000
    print(Alex)
elif x=='Kate'or'kate':
    Kate = Kate[1]+1000
    print(Kate)
else:
    print('That is not an employee')