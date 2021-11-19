import turtle
p1=turtle.Pen()
p2=turtle.Pen()
p1.forward(220)
p2.left(45)
p2.forward(300)




class instrument:
    def roditel(self):
        print('salo')
   
class ruchki(instrument):
    pass
class kisti(instrument):
    def __init__(self,price):
        self.myprice = price
    def readprice(self):
        print(self.myprice)
    def writeprice(self,newprice):
        self.myprice=newprice
    def kto(self):
        print('ya kistochka')
    
obj1=kisti(200)
obj1.kto()
obj1.roditel()
obj1.readprice()
obj1.writeprice(500)
obj1.readprice()
