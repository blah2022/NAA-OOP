class Parallelogram:
    def _init_(self,a,b):
       
        if a <= 0 or b<= 0 :
            raise Exception('Bases (a) and side (b) of parallelogram must be positive numbers!')
        self.a = a
        self.b = b

    def perimetr (self):
        
        return 2*(self.a + self.b)
    def area (self):
        
        return self.a*self.b
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
obj = Parallelogram(a,b)
print("Perimetr of Parallelogram :", obj.perimetr())
print("Area of Parallelogram :", obj.area())