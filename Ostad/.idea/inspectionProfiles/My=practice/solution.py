"""fruits =['apple', 'banana', 'cherry', 'berry', 'kerry', 'merry', 'serry', 'gerry','/n' ,'\n']
for i in range(8):
    print(i,fruits[i] )

fruits = ['apple', 'banana', 'cherry', 'berry', 'kerry', 'merry']
for i in range(6):
    print(i, fruits[i])

for i in "amicabli":
    print(i)

for i in ("Banana"):
    print(i)

for i in "1000:":
    print(i)
"""
#generate multiplicatiion table 
def generate_multiplicfation_table(n):
    print(n, "x n =", n*1)
    print(n, "x n =", n*2)
    print(n, "x n =", n*3)
    print(n, "x n =", n*4)
    print(n, "x n =", n*5)
    print(n, "x n =", n*6)
    print(n, "x n = ", n*7)
    print(n, "x n =", n*8)
    print(n, "x n =", n*9)
    print(n, "x n =", n*10)

n = int(input("Enter your number: "))
generate_multiplicfation_table(n)
