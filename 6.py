class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def setCoords(self,x,y):
        self.x = x
        self.y = y           
    def __del__(self):
        print('udal')

pt = Point(4)
print(pt.__dict__)
pt.setCoords(5,6)
print(pt.__dict__)
pt2 = Point(3)
print(pt2.__dict__)

