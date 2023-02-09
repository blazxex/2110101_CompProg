
import math
a = float(input())
temp = a
l=0
u = 0
while temp!=0:
    temp = temp/10
    u+=1
    
x=(l+u)/2

while not (abs(a-x**2) <= 10**(-10)*max(a,x**2)):
    if x**2 > a:
        u=x   
        x = (l+x)/2
    elif x**2<a:
        l=x
        x = (x+u)/2
        
print(1+round(math.log10(x),6))