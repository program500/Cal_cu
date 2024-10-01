#object orinted programming 
x = 5 
y = 5.54
z = True 
        
print(dir(x))
print(x.numerator)
print(x.bit_count())

my_list = [1,2,3]

my_list.append(5)
print(my_list)

# if i want to create a class iself 
class A:
    total = 6
def say_hello():
    print("HElllo ;;")
print(A.total)

print(A)
obj1 = A()
print(obj1)

#constractor 
class Fraction:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom
        print("Hi, I am here")

def __str__(self):
    return "{}/ {}".format()

def my_function():
    x = 10 
    t = 34
    y = x + t
    print(y)
my_function()


