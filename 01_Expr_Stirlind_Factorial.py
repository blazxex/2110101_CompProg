import math
n = int(input())
def low(n):
    x = math.sqrt(2*math.pi)*(pow(n,n+(1/2)))*(pow(math.e,-n+(1/(12*n+1))))
    return x
def high(n):
    y = math.sqrt(2*math.pi)*(pow(n,n+(1/2)))*(pow(math.e,-n+(1/(12*n))))
    return y
print(low(n))
print(high(n))
