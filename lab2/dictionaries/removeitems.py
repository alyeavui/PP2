#example 1
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
thisdict.pop("model")
print(thisdict)

#example 2
thisdict.popitem()
print(thisdict)

#example 3
del thisdict["model"]
print(thisdict)

#example 4
thisdict.clear()
print(thisdict)
