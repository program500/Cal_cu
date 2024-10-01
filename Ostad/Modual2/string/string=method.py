#string method 
text = "Hello World"
print(text.upper())
print(text.lower())
print(text.islower())
print(text.isdigit())
print(text.capitalize())

print(text.swapcase())
print(text.istitle())
print(text.replace('World', 'python'))

text = "Hello-world-with-python"
print(text.split("-"))
print("-".join(text))

print("Hello world")

#check if string starts with a substring 
text = "Hello world"
print(text.startswith("Hello"))
print(text.endswith("world"))
print(text.endswith("Hello"))

#Find the Possition of a substring 
text = "Hello python "
print(text.find("python"))
space = " "
print(text.isspace())
print(space.isspace())

#count occurrences of a substring 
Hasip = "Hello world"
print(Hasip.count("o"))  
print(Hasip.index("o"))   # I have learnt a lot of things hahhahahah hah aha haha aha ahha

#check if all charaeters are alphanumeric 
print(text.isalnum())

text = " 1,2,3,4,5,6,7,8,9"
print(text.isalnum())

print(text.isalpha())

text1 = "Hello123"
print(text1.isalnum())
text2 = "Hello"
print(text2.isalnum())

text3 = "123456789"
print(text3.isalnum())
text = " "
print(text.isalnum())

#check if al charecter isalpha
text4 = "Hello"
print(text4.isalpha())

text5 = "Hello13"
print(text5.isalpha())

text = "Hello "
print(text.isalpha())
text = " "
print(text.isalpha())
print(text.isspace())



#string method type data 
text = "Hello world "
print(text.strip("H").upper())

"""
use case:
Data cleaning, Formating, text analysis, user input processing 
Generateing dynamic text.
"""