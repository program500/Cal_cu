
#contorl flow type data 
marks = int(input("Enter your marks: "))
if marks <= 100 and marks >= 80:
    print("A+")
elif marks <= 80 and marks >= 70:
    print("A")
elif marks <= 70 and marks >= 60:
    print("A-")
elif marks <= 60 and marks >= 50:
    print("B")
elif marks <= 50 and marks >= 40: 
    print("C")
elif marks <= 40 and marks >= 33:
    print("D")
else:
    print("F")