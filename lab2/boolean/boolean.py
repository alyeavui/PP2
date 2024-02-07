#example 1
print(6 < 5)
print(6 == 5)
print(6 > 5)

#example 2
a = 7
b = 30

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#example 3
print(bool("Ayau"))
print(bool(18))

#example 4
x = "Ayau"
y = 18

print(bool(x))
print(bool(y))

#example 5
bool("ayau")
bool(111)
bool(["cat", "dog", "bird"])

#example 6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#example 7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#example 8
def myFunction():
  return True

print(myFunction())

#example 9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#example 10
x = 21
print(isinstance(x, int))
