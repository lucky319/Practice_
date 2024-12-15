# __add__ method 
class Test:
    
    def __init__(self, a ,b):
        self.a = a
        self.b = b
        
    def __add__(self):
        return f"Adding a and b values : {Test(self.a, self.b)}"
    def __str__(self):
        return f"m str Method Test({self.a}, {self.b})"
    
t1 = Test(20,30)
print(t1)
print(t1.__add__())
t2= Test(4,5)
print(t2)


print("adding this line to commit from account1!")
print("Adding this line to commit from account1 and lakshmi and Test branch")