class Cars:

    def __init__(self,brand_name,price,type,colour):
        self.brand_name = brand_name
        self.price = price
        self.type = colour
car1 = Cars('Ferrari',230000,'F8','Red')
car2 = Cars('BMW',150000,'i8','Grey')
car3 = Cars('Lamborghini',253000,'Urus','Blue')

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)