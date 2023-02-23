import math
par = 0
stroke = 0
adjust = 0
for i in range(9):
    a,b,c=input().split()
    par += int(a)
    stroke += int(b)
    if int(c) == 1:
        adjust+=min(int(a)+2,int(b))

fixPoint = math.floor(0.8*((1.5*adjust)-par))
point = stroke - fixPoint
print(stroke)
print(fixPoint)
print(point)
        
    