class Point:
    def __init__(self,x=0,y=0):
        self.__x=x 
        self.__y=y


    def Setcords(self,x): 
        self.__x = x
        
    def Getcords(self):   
        return self.__x
       

    def Delcords(self):
        print('delete')
        del self.__x    
         
    coordx = property(Getcords, Setcords, Delcords) # запись чтобы проще пользоваться геттерами и сеттерами касательно х прописано в классе!!!!!!!!!!!!!!!!!!

pt = Point(1,2)

pt.coordx = 5#запись значения


print(pt.__dict__)

del pt.coordx# удаление значения

print(pt.__dict__)
pt.coordx = 8 # запись значения

print(pt.__dict__) 

print(pt.coordx)# вывод значения