# Print first 10 sastry numbers
import math
p = 0
x = 0
u = 0
while p != 10:
    u = u+1
    x = int(x)
    x = x+1
    y = x+1
    x = str(x)
    y = str(y)
    z = x+y
    z = int(z)
    s = math.sqrt(z)
    if s%2 == 0:
        print(x)
        p = p+1
print(u)