class Point:
    x = 1
    y = 1
    def setCoords(self):
        print(self.__dict__)
pt = Point()
pt.x = 2
pt.y = 3    
pt.setCoords()