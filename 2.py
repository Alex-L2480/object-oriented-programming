
class Dog:
    'opisanie'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title() + ' sit')    
    def jump(self):
        print(self.name.title() + ' jump')
my_dog = Dog('Stone',5)
print(my_dog.name)    
my_dog2 = Dog('Rex',3)
my_dog.sit()
my_dog2.jump()
print(Dog.__doc__)
print(my_dog.__dict__)
print(getattr(my_dog2,'age',False))
print(getattr(my_dog2,'ag',False))
setattr(my_dog,'height',10)# add atribute
print(my_dog.__dict__)
print(isinstance(my_dog,Dog))# проверка на причастность к классу 