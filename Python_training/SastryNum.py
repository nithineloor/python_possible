# Find out if the user input is a sastry number
# import math module
import math
# user enter number
x = int(input())
# userNum +1
y = x+1
# Convert to string
x = str(x)
y = str(y)
# Concantenate
z = x+y
# Convert back to Int
z = int(z)
# find Sqare root
s = math.sqrt(z)
# Check if num is even and print
if s%2 == 0:
    print("This is a sastry number") 
else:
    print("This is not a sastry number")