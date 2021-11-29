import matplotlib.pyplot as plt


y = [10, 25, 25, 15]
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

myexplode = [0.2, 0, 0.2, 0]
plt.pie(y, labels = mylabels, explode = myexplode)

plt.legend(loc = 'lower right')

plt.show()