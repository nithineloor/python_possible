class Dogs:

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
dog1 = Dogs('Harry',6,'Mini pou')
dog2 = Dogs('Percy',5,'Malti pou')
dog3 = Dogs('Luke',6,'Golden Retriever')
print(dog1.__dict__)
print(dog2.__dict__)
print(dog3.__dict__)
print(dog1.name)
print(dog1.breed)