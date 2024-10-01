#loop dictionary type data 


examresult = {"Bangla":95, "English": 89, "Math":89}
for subject, marks,  in  examresult.items():
    print(subject)
    print(marks)


biodata = {
           "Name": "Abid Hasan", 
    
           "Roll": 3, 
            
            "age": 20, 
            "city": "Dhaka"
}

for keys,values in biodata.items():
    print(keys)
    print(values)
    print(keys,values)
    print(keys[0])
    print(values[0])


my_dic = {
         "Name": "Abid",
         "age": 20, 
         "city": "San francisco"
}

for keys, values in my_dic.items():
    print(keys)

