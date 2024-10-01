"""class Father: 
    x = 10 
    y = 20 
    def __init__(self):
        print("Father constructor")
    
def add(self):
    print(self.a+self.b)

class son (Father):
    pass 
obj = Father()
obj1 = son()
"""

"""class Father: 
    x = 10 
    y = 230 
    def __init__(self):
        super(). __init__()
        print("Father constructor ")
    def add(self):
        print(self.x+self.y)
class son(Father):
    def __init__(self):
        super(). __init__()
        print("son Constructor")



objt = son()
obj = Father()"""

#if babab and cheler kache constructor thake taile banar ta bana use korte parbe cheler ta chele use lkorter parbe
#in chele use korte cay cheler ta and babar ta taile code hobe arokom to lest start
class Father: 
    x = 10 
    y = 20 
    def __init__(self):
        print("Father constructor")
        print(f"Our modulus is {self.x%self.y}")
class son(Father): 
    a = 100 
    b = 200
    def __init__(self):
        super().__init__()
        print("Son constructor")
        print(f"Our result is {self.a+self.b}")

so = son()