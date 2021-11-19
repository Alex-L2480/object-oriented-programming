class Point:
    def __init__(self,x=0,y=0):
        self.__x=x #защищенные данные принт пт.х не выведешь
        self.__y=y

    def __Chekvalue(i):# приватный метод
        if isinstance(i,(float, int)):
            return True
        else:
            return False



    def Setcords(self,x,y):
        if Point.__Chekvalue(x) and Point.__Chekvalue(y):
            self.__x=x
            self.__y=y
        else:
            print('no digit')

    def Getcords(self):#выводим защищенные данные публичным методом
        return self.__x,self.__y


pt = Point(1,2)
print(pt.Getcords())
pt.Setcords(3,18)
print(pt.__dict__)
print(pt.Getcords())
print(pt._Point__y)# обращение к приватной переменной вывод ее
