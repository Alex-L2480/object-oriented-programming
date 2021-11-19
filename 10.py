class Human: #создаю класс
    default_name = 'No name' #статические поля
    default_age = 0

    def __init__(self,name = default_name ,age = default_age):
        #Динамические поля
        ##Публичные
        self.name = name
        self.age = age 
        ##Приватные
        self.__honey = 0
        self.__mouse = None
    def info(self):# вывод всей информации об объекте
        print(self.__dict__)
    #Приватный метод
    def __make_deal(self,mouse,price):
        self.__honey -= price
        self.__mouse = mouse

    def earn_honey(self,amount):
        self.__honey += amount

    def buy_mouse(self, mouse, discount):
        price = mouse.final_price(discount)
        if self.__honey >= price:
            self.__make_deal(mouse, price)
            print('Deal')
        else:
            print('No honey')

class Mouse:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self, discount):
        final_price = self._price *(100-discount)/100
        print(final_price)
        return(final_price)

class Smallmouse(Mouse):
    def __init__(self, price):
        super().__init__(40, price)

a = Human('Fedor', 32)
a.info()
b = Human('Pes')
b.info()
a.earn_honey(10000)
a.info()

m = Mouse(100,15000)

a.buy_mouse(m,40)

a.info()

s= Smallmouse(8500)
c = Human('Ed',25)
c.earn_honey(10000)
c.buy_mouse(s,10)
c.info()



