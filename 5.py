class Point:
  def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
  def setCoords(self,x,y):
        self.x = x
        self.y = y    
pt = Point(4)
print(pt.__dict__)
pt.setCoords(5,6)
print(pt.__dict__)