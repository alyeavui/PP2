x = "cool"

def firstfunc():
    print("Ayau is " + x)

firstfunc()

y = "Python"
def secondfunc():
    y = "C++"
    print("I love " + y)

secondfunc()

print("I love " + y)

def thirdfunction():
    global z
    z = "example"

thirdfunction()
print(z)

w = "global 1"
def fourthfunction():
    global w
    w = "global 2"

fourthfunction()
print(w)