class Composite:
    def __init__(self, one = 1, two = 2):
        self.one = one
        self.two = two
        
        
    def add(self):
        return self.two +self.one
        
class Component:
    def __init__(self):
        self.base = Composite()
        
    def multiply(self):
        return self.base.one * self.base.two
    
component = Component()
print(component.base.add())
print(component.multiply())
