class Employees:# Making the class and naming it
	
	def __init__(self, name, age, salary):# initializing object parameters
		self.name = name #mapping object parameter
		self.age = age
		self.salary = salary
		


emp1 = Employees('ron', 35, 24000)#making class object
emp2 = Employees('Neil', 40, 20000)

print(emp1.__dict__)#printing all emp1 and emp2 details
print(emp2.__dict__)

print(emp1.name)#printing only emp1 name and salary
print(emp1.salary)