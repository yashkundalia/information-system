class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        A=self.x * self.y
        print(A)
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
class square:
    def __init__(self,x):
        self.x = x
    def area(self):
        A=self.x * self.x
        return self.x * self.x
    def peri(self):
        return 2 * self.x + 2 * self.x
class cube:
    
    def __init__(self,x):
        self.x = x
    def area(self):
        return self.x * self.x*6
    def peri(self):
        return 12*self.x
    def vol(self):
        return self.x *self.x *self.x
class sphere:
    
    def __init__(self,x):
        self.x = x
    def area(self):
        A=self.x * self.x * 4 *3.14
        return A
    def vol(self):
        return self.x * self.x * 4 *3.14 /3 *self.x
    

