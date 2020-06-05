# 3、 圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。
# 解决思路：
# （1）、首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用。
# （2）、在定义圆形类时，要处理可能产生的异常。要求：输入的圆环类内、外半径必须是数值型数据类型，内部圆半径要比外部圆半径要小，
# 如果不满足这些条件，则需要处理异常。
class Circle:
    def __init__(self,r,PI=3.14):
        self.r = r
        self.PI = PI
    def C(self):
        c = 2*self.PI*self.r
        print(c)
    def S(self):
        s = self.PI*self.r*self.r
        print(s)

c1 = Circle(input("请输入圆的半径："))

class Ring:
    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2