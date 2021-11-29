num=[6,3,4,1,5,2]

print('Enter a number')

x = int(input())

num.append(x)

num.sort()

z = max(num)

y = min(num)

i = sum(num)

print('the sum of all numbers in your list is ',i)

print('the smallest number is',y)

print('the largest number is ',z)

print(num)