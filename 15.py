class Point:

    __slots__ = ['x','y','p']# разрешенные атрибуты

    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __Chekvalue(i):# приватный метод
        if isinstance(i,(float, int)):
            return True
        else:
            return False

    def Setcords(self,x,y):
        if Point.__Chekvalue(x) and Point.__Chekvalue(y):
            self.x=x
            self.y=y
        else:
            print('no digit')

    def Getcords(self):#выводим защищенные данные публичным методом
        return self.x,self.y

    
pt = Point(1,4)
print(pt.x)
pt.p=7  
print(pt.p)



