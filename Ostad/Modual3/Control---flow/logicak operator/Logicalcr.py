"""#Logical operator type data 
day = str(input("Enter your day: "))
print(day == "Saturday" or day == "Friday")
if day == "Friday" or day == "Saturday":
    print("Today is holiday.")           #it is logic  operator 
else:
    print("I have to go to office today ")

"""
"""#logical operator
today = input()
print(today == "Sunday" or today == "Saturday")
if  today == "Sunday" or today == "Saturday":
    print("No office today. ")
else:
     print("I have to go to office today")
public_holiday = True
is_sick_today = True

"""
#logical operator 
today = input("Enter your day: ")
public_holiday = input("Is it a public holiday? (yes/no) ")
public_holiday = public_holiday.lower()
is_sick_today = input("are you sick today (yes/no)")

print(today = "Sunday" or today == "Saturday")
if today == "Sunday":
     print("No office today")
elif today == "Saturday":
     print("No office today")
elif public_holiday:
     print("No office today")
elif is_sick_today:
     print("No office today")
else:
     print("I have to go to office today")



