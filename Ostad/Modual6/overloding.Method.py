"""class Father:
    x = 10 
    y = 29 
    def addtwo(self, x, y):
        print(self.x+self.y)
    def addtwo1(self, a, b):
        print(self.a-self.b)
obj = Father()
obj.addtwo()"""

"""#Overloding optional paramitars 
class Father: 
    x = 10 
    y = 40 
    def addtwo(self, a=0 , b=0 ,c =0 , d=0  ) :
        print(self, a, b, c, d)
obj = Father()
obj.addtwo()
obj.addtwo(10)
obj.addtwo(10, 10)
obj.addtwo(10, 10, 10, )
obj.addtwo(10, 10, 12, 42)

#Method over loding variable lenth argument 
class Father: 
    def method(self, *x):
        print(x)
        print(type(x))
ob= Father()
ob.method(1)
ob.method(1, 2)
ob.method(1,2,3)
ob.method(1,2,3,4,5,6,7,8,9)


#Over loding optional paramitar
class Ba: 
    def function(self, a=0, b=0 , c= 0 , d= 0):
        print(self, a, b,  c, d)
ob = Ba()
ob.function(10)
ob.function(10,20)
ob.function(10,20,39)
ob.function(10, 20, 30,43)


#over loding type data 
class my: 
    def sm(self, a= 0 , b = 0 , c = 0 , d = 0 , e =  0 ): 
        print(self,a,b, c,d, e)

ob = my()
ob.sm(10,29,40,40,30)
ob.sm(5)
ob.sm(6)



#over loding variable lenth argument 
class Father: 
    def method(self, *x ): 
        print(x)
        print(type(x))

ob = Father()
ob.method(1)
ob.method(1,2)
ob.method(12,4,)
ob.method(1,2,3,4,5,6)
ob.method(2,3,4,5,6,7,8)"""

#python lenth argument type data 
class GrandFather: 
    def method(self,*b): 
        print(b)
        print(type(b))
c = GrandFather()
c.method(12)



#python lenth argument type data






class ourChanel: 
    def chanel(self, *c): 
        print(c)
        print(type(c)) #over loding lenth argument type data 
ob = ourChanel()
ob.chanel(10,20)
ob.chanel(10,20,30,40,50,60,70,80)
print(ob.chanel(1000))



