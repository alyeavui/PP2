#1
import math
d = int(input())
r = float()
r = d * (math.pi/180)
print(r)

#2
h = int(input())
b1 = int(input())
b2 = int(input())
area1 = ((b1 + b2)/2) * h
print(area1)

#3
sides = int(input())
length = int(input())
area2 = (sides * length)/(4 * math.tan(math.pi/sides))
print(area2)

#4 
base = int(input())
height = int(input())
area3 = base * height
print(area3)
