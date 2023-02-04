import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]


def checkMonth(m,y):
    if m==4 or m==6 or m==9 or m==11:
        m=30
    elif m!=2:
        m=31
    elif m==2:
        if y%400 ==0:
            m=29
        elif y%4==0 and y%100!=0:
            m=29
        else:
            m=28
            
    return m

def day_of_year(d,m,y):
    doy=0
    for i in range(1,m):
     doy += checkMonth(i,y-543)
    return doy+d
def checkYear(y):
    if y%400 ==0:
            y = 366
    elif y%4==0 and y%100!=0:
        y = 366
    else:
        y = 365
    return y

def sumYear(by,y):
    sum=0
    for i in range(by,y+1):
        sum+=checkYear(i)
    return sum

day = day_of_year(bd,bm,by)+sumYear(by,y)




    





def day_of_year(d,m,y):
    doy=0
    for i in range(1,m):
     doy += checkMonth(i,y-543)
    return doy+d