def my_function(a,b):
    num1 = a 
    num2 = b         #single value return 
    sum = num1 + num2
    return sum
result= my_function(10,20)
print(result)

#multiple function return type data 

def myfunction(a,b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    fd  = num1 // num2    #From the rabbils sir video i have learnt that
                          #how to discover a lot of funtion 
                          # and how to return single funtion and multiple funtion 
    exp = num1 ** num2 
    bol = num1 <= num2
    gr = num1 > num2
    le = num1 < num2
    dq = num1 == num2
    return sum, sub, mul, div, fd, exp, bol, gr, le, dq
v = myfunction(10, 20)

print(v) 
print(type(v))

#list return function type  data 

def my_production(a,b):
      num1 = a 
      num2 = b
      adi = num1 + num2
      sub = num1 - num2
      mul = num1 * num2
      exp = num1 ** num2 
      mod = num1 % num2 
      div = num1 / num2         #list function type data 
      fd = num1 // num2
      gr = num1 < num2
      les = num1 > num2
      dq  = num1 == num2   #this is hasip who has learnt a lot of information about programming from Rabbil sir 

      gq = num1 <= num2    #this is prove 
      lq = num1 >= num2
      return [adi, sub, mul, exp, mod, div, fd, gr, les, dq, gq, lq]  
var = my_production(2,4)
print(var)

def addtwo(a, b):
     num1 = a 
     num2 = b 
     sum = num1 + num2
     sub = num1 - num2
     mul = num1 * num2 
     div = num1 / num2
     return {"sum":sum, "sub":sub, "mul":mul, "div":div}
my_all_information = addtwo(10, 20)
print(my_all_information)

#loop function return type data
def first_even_number(numbers):
    for number in numbers:
        if number  % 2 == 0:      #using return early exit 
            return number
         
        return None 
every = first_even_number([1,2,3,4,5,6,7,8,9,0])
print(every)

def myfuntion_vp(a, b):
    x = a 
    y  = b 
    bd = x + y, 
    return bd 
var = myfuntion_vp(10,20)
print(var)
print(type(var))

def myall_function(x, y ):
    a = x 
    b = y 
    adi = x + y 
    mul = x * y 
    sub = x - y 
    div = x / y                #This is a return type data 
    fldi = x // y 
    exp  = x ** y 
    mod = x % y 
    gr = x > y 
    lg = x < y 
    gq = x <= y 
    lq = x >= y 
    dq  = x == y
    return  [adi, mul, sub, div, fldi, exp, mod, gr, lg, gq, lq, dq ]

math = myall_function(3,6)

print(math)

#loop return type data 
def my_first_number(numbers):
    for number in numbers:             #none type data 
        if number % 2 == 0:
            return number
        return None
var = my_first_number([1,2,3,4,5,6,7,8,9,0])
print(var)





#function return type data 
def my_second_function(a,b):
    x = a 
    y = b 
    adi = a + b 
    sub = a - b 
    mul = a * b 
    exp = a ** b 
    div = a / b 
    gr = a < b 
    ls = a  > b 
    eq = a == b 
    gq = a <= b 
    lq = a >= b 
    fd = a // b 
    return [adi, sub, mul, exp, div, gr, ls , eq, gq, lq, fd  ]
mack = my_second_function(1,2)
print(mack)



def my_third_function(a,b):
    x = a 
    y = b 
    addi = a + b 
    subs = a - b 
    return (addi, subs)
substraction = (5,6)
print(substraction)

print(((((((((((((((((((((((((((((((((((((((((((((((((("Hello world "))))))))))))))))))))))))))))))))))))))))))))))))))

def my_new_folder(a,b):
    x = a 
    y = b 
    sum = x + y 
    sub = x - y 
    mul = x * y 
    ex  = x ** y 
    gr = x < y 
    les = x > y 
    eq = x == y 
    return {sum,sub,mul,ex,gr,les,eq}
result = my_new_folder(2,4)
print(result)
print(type(result))



def my_all_function(a,b):
    x = a 
    y = b 
    sum = x + y 
    sub = x - y 
    mul = x * y 
    div = x / y 
    ex  = x ** y 
    fd = x // y 
    gr = x > y 
    ls = x < y 
    dq = x == y 
    eg = x >= y 
    el = x <= y 
    return [sum,sub,mul,div,ex,fd,gr,ls,eg,el]
my = my_all_function(2,4)
print(my)
my_all_function()


def my_function_number(a, b):
    x = a 
    y = b 
    adi = x + y
    sub = x - y
    mul = x * y
    div = x / y 
    exp = x ** y 
    fd = x // y
    gr = x > y
    ls = x < y 
    gq = x >= y 
    lq = x <= y 
    dq = x == y 
    return[adi, sub, mul, div, exp, fd, gr, ls, gq, lq, dq]
our = my_function_number(2, 4)
print(our)
my_function_number()
