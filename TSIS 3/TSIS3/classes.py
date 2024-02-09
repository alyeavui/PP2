#task 1
class mystring: 
    def __str__(self, String): 
        self.String = String 
    def getString(self): 
        self.String = input() 
    def printString(self): 
        print(self.String.upper()) 
mystr = mystring() 
mystr.getString() 
mystr.printString()

#task 2
class Shape: 
    def __init__(self, length): 
        self.length = length 
 
    def area(self): 
        return 0 
 
class Square(Shape): 
      
    def area(self): 
        return self.length ** 2 
areashape = Shape(0)   
areasquare = Square(5) 
 
print(areashape.area())   
print(areasquare.area())

#task 3
class Shape: 
    def __init__(self, length): 
        self.length = length 
class Rectangle(Shape): 
    def __init__(self, length, width): 
        self.length = length  
        self.width = width  
    def area(self): 
        return self.length * self.width  
area = Rectangle(5, 10) 
print(area.area())

#task 4
import math 
class Point: 
    def __init__(self, x, y): 
        self.x = x  
        self.y = y  
    def show(self): 
        print(self.x, self.y) 
    def move(self, x1, y1): 
        self.x = x1  
        self.y = y1  
    def dist(self, otherpoint): 
        distance = math.sqrt((self.x-otherpoint.x)**2 + (self.y-otherpoint.y)**2) 
        return distance 
point1 = Point(2,5) 
point2 = Point(3,4) 
point1.show() 
point2.show() 
point1.move(1,2) 
point1.show() 
distance = point1.dist(point2)  
print(distance)

#task 5
class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Funds unavailable!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted")

acc1 = input()
acc2 = int(input())
account = Account(acc1, acc2)

d = int(input())
account.deposit(d)
print("Current balance after deposit:", account.balance)

w = int(input())
account.withdraw(w)
print("Current balance after withdrawal:", account.balance)

account.withdraw(acc2 + d)

#task 6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = input()
num_list = list(map(int, numbers.split()))

prime_numbers = list(filter(lambda x: is_prime(x), num_list))
print(prime_numbers)


