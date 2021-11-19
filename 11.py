class Point:
    def __init__(self,x=0,y=0):
        self.__x=x #защищенные данные принт пт.х не выведешь
        self.__y=y

    def Setcords(self,x,y):# меняем защищенные данные публичным методлом
        if isinstance(x,(float, int)) and isinstance(y,(float, int)):#проверка на цифры
            self.__x=x
            self.__y=y
        else:
            print('no digit')

    def Getcords(self):#выводим защищенные данные публичным методом
        return self.__x,self.__y


pt = Point(1,2)
print(pt.Getcords())
pt.Setcords(3,4)
print(pt.__dict__)
print(pt.Getcords())