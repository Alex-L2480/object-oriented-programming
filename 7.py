class Point:
    def __init__(self,x=0,y=0):
        self.__x = x# __защищает аргумент
        self.__y = y
    def setCoords(self,x,y):
        if (isinstance(x,int) and isinstance(y,int)):
            self.__x=x
            self.__y=y
        else:
            print('no digit')    
    def getCoords(self):
        return self.__x,self.__y
pt = Point(1,2) 
pt.setCoords(3,'y')
print(pt.__dict__)
print(pt.getCoords())
