#1
import math
n = int(input)
for i in range(1, n + 1):
    print(math.pow(i, 2))

#2
m = int(input())
for i in range(1, m):
    if(i % 2 == 0):
        print(i, sep = ", ")

#3
a = int(input())
for i in range(0, a + 1):
    if(i % 4 == 0) & (i % 3 == 0):
        print(i)

#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)


#5
def countdown(n):
    while (n >= 0):
        yield n
        n -= 1

n = int(input())
for i in countdown(n):
    print(i)