class Color():
    def __init__(self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    def ppp(self):
        return self.height*self.width*self.length
c1 = Color(10,10,10)
c1.ppp()
print(c1.ppp())