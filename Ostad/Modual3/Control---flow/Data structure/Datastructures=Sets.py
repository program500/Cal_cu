#Data structure sets type data
fruits = {'apple', 'banana','cherry'}
fruits.add("mango")
print(fruits)
fruits.update(['berry'])
print(fruits)

sett1 = {"Guava", "Date", "Guava", "Date",  "Jackfruit"}
sett2 = {"Plum", "Pineapple", "Onion"}
result = sett1.intersection(sett2)
print(result)

#we can search common value
set = {1,3,4,3,4,5}
set1 = {1,3,3,4,5,4}
eventually = set.intersection(set1)
print(eventually)

eventually = set.difference(set1)

print(eventually)
eventually = set.issubset()

eventually = set1.issuperset()
print(eventually)
