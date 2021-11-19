class Point:
    WIDTH = 5
    def __init__(self,x=0,y=0):
        self.__x = x# __защищает аргумент
        self.__y = y
    def __checkvalue(x):
        if isinstance(x,int):
            return True
        return False
    def setCoords(self,x,y):
        if Point.__checkvalue(x) and Point.__checkvalue(y):
            self.__x=x
            self.__y=y
        else:
            print('no digit')    
    def getCoords(self):
        return self.__x,self.__y
    def __getattribute__(self,item):
        if item=='_Point__x':
            return 'Chastnaya premennaya'
        else:
            return object.__getattribute__(self,item)    
    def __setattr__(self,key,value):
        if key == 'WIDTH':
            raise AttributeError #выдает ошибку при попытке поменять 
        else:
            self.__dict__[key] = value

pt = Point(1,2) 
pt.setCoords(3,'7')
print(pt.__dict__)
print(pt.getCoords())
pt.WIDTH = 9
print(pt.WIDTH)