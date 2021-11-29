#Write a program to manage the stock ans billing in a supermarket
items = ['Water','chips']
rate = [2,5]
quantity_in_stock = [20,30]
bill = []

print('What would you like to buy')
print('Water $2 or chips $5')
print('There is',quantity_in_stock[0],'waters in stock and',quantity_in_stock[1],'chips in stock')
x = input()
print('How many ?')
k = int(input())
if x == 'Water' or x == 'water':
    quantity_in_stock[0] = quantity_in_stock[0] - k
    priceWater = rate[0]*k
    bill.append(priceWater)
    print('Purchase or back')
    y = input()
    if y == 'purchase' or y == 'Purchase':
        print("Thank you for shopping")
    else:
        print('Bye')
elif x == 'chips' or x == 'Chips':
    quantity_in_stock[1] = quantity_in_stock[1] - k
    priceChip = rate[1]*k
    bill.append(priceChip)
    print('Purchase or back')
    i = input()
    if i == 'purchase' or i == 'Purchase':
        print('Thank you for shopping')
    else:
        print('Bye')
else:
    print('Sorry not in stock')


bill.append(x)
print(bill)