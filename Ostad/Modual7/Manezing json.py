#python object ke json file a convert 
import json
"""person = {
    "name": "HAsip", 
    "age": 20, 
    "city": "Sanfrancisco",
    "Hasjchild": False,
    "titles": ["engineer","program"]
}

personjson =json.dumps(person , indent=4)
print(personjson)
print(personjson['age'])"""

"""
person={
    "name": "Hasip", 
    "age": 20, 
    "city": "Dhaka", 
    "man": True, 
    "profesion": ["engineer", "programmer"]

}

perosnobs = json.dumps(person, indent=4)
print(perosnobs)"""

"""
#python object ke jona convert with 10 minute 

person = {
    "name":"Hasip", 
    "age": 20, 
    "city": "Dhaka", 
    "Man": True, 
    "profession" : ["engineer", "programmer"]
}

personjson = json.dumps(person, indent=4)
print(personjson["name"])"""

##json string ke convert korbo python dic or object a 
"""person = {
    "name": "Hasip", 
    "age": 20 , 
    "city": "Dhaka", 
    "man": True, 
    "profession": ["engineer", "programmer"]

    
}

personjson = json.dumps(person, indent=5)
print(type(personjson))
print(personjson)
"""

"""sp = open("text", "w") 
text.write("Hello world ")6"""

my_tuple = ("apple", "banan", "cerry", "berry", "coconut")
for index , items in enumerate(sorted(my_tuple), start=1): 
    print(f"{index}.{items}")


for i in range(10, 50, 5):
    

    print(i)

