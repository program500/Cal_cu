# I have to convert in json  which python object 

"""person = { 
    "Name": "Hasip", 
    "age": 20 , 
    "city" : "Dhaka ", 
    "vari": True, 
    "profession": ["engineer", "programmer"]
}

personjson = json.dumps(person, indent=5)
print(personjson)

 
"""

"""#json string ke korbo in convert python object 
import json 

personjson  ={"Name": "Abid", "age":20, "city":"sanfrancisco"}

personobj = json.loads(personjson)

print(personobj)

 """

#pytho object ke json string a convert korbo and json string ke json file write korbo 

#We have to three work 
import json
pythonobj = {
    "Name": "Hasan", 
    "age": 20 , 
    "city": "Sanfrancisco", 
    "profession": ["engineer", "programmer"]
}

pythonjson = json.dumps(pythonobj, indent= 5) 

print(pythonjson)

with open("person.json", "w") as pythonjsonfile: 
    json.dump(pythonjson,pythonjsonfile, indent=4)
print("Create success")

