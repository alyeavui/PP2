#example 1
x = lambda a : a + 10
print(x(5))

#example 2
x = lambda a, b : a * b
print(x(5, 6))

#example 3
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#example 4
def myfunc(n):
    return lambda a : a * n

#example 5
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

#example 6
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

#example 7
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))