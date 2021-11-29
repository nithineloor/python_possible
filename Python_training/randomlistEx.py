import random

l2=[]
l2 = random.sample(range(1000, 5000), 1000)
l3 = [l2[1]]
l2.append(l3[0])
print(l2)
print(len(l2))
new_set=set(l2)
print(len(new_set))
# token1 = secrets.token_bytes(10) 
# print(token1)