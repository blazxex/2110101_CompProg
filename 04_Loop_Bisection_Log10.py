import math
a = float(input())
l=0
u=a
x = (l+u)/2
while not (abs(a-x**2) <= 10**(-10)*max(a,x**2)):
    if x**2 > a:
        u=x   
        x = (l+x)/2
    elif x**2<a:
        l=x
        x = (x+u)/2
        
print(round(math.log10(a),6))
    