#example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = thisdict["model"]

#example 2
x = thisdict.get("model")

#example 3
x = thisdict.keys()

#example 4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(x) 
car["color"] = "white"
print(x) 

#example 5
x = thisdict.values()

#example 6
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.values()
print(x) 
car["year"] = 2020
print(x) 

#example 7
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.values()
print(x) 
car["color"] = "red"
print(x)

#example 8
x = thisdict.items()

#example 9
x = car.items()
print(x) 
car["year"] = 2020
print(x)

#example 10
x = car.items()
print(x) 
car["color"] = "red"
print(x)

#example 11
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


