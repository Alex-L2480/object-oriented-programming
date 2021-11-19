class Point:

    W=5# константа, которую нельзя менять

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


    def __getattribute__(self,item):# Перегружаем метод геттатрибут, так, что при запросе х высветится приват дата
        if item == '_Point__x':
            return 'Private data'
        else:
            return object.__getattribute__(self,item)

    def __setattr__(self,key,value):# перегрузка метода сеттатр так, чтобы W не менялось - вылетала ошибка
        if key == 'W': # 'W' писать в кавычках
            print('No change  W')
        else:
            self.__dict__[key] = value    



pt = Point(8,8)  
setattr(pt,'p',7)
print(pt.__dict__)
setattr(pt,'W',6)

pt.zzz=5 #добавление атрибута
print(pt.__dict__)

del pt.zzz #удаление
print(pt.__dict__) 