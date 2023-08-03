import math
bd, bm, by, d, m, y = [int(e) for e in input().split()]

def checkMonth(m,y):
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    day1=28
    y=y-543
    if m == 2:
        if y%400 ==0:
            day1=29
        if y%4==0 and y%100!=0:
            day1=29
    else :
        day1=month[m-1]
        
 
    return day1

def checkRed(d,m,y):
    sumDay = 0
    for i in range(m+1,13):
        sumDay+= checkMonth(i,y)
    day3 = checkMonth(m,y)-d+1+sumDay
    return day3
    
def checkBlue(d,m,y):
    sumDay = 0
    for i in range(m-1,0,-1):
        sumDay+= checkMonth(i,y)
    day2 = sumDay+d-1
    return day2
    



black_date= (y-by-1)*365
red_date = checkRed(bd,bm,by)
blue_date = checkBlue(d,m,y)
sum = black_date+red_date+blue_date
physical = math.sin(((2*math.pi*sum)/23))
emotional = math.sin(((2*math.pi*sum)/28))
intellectual = math.sin(((2*math.pi*sum)/33))
print(sum,"{:.2f}".format(physical),"{:.2f}".format(emotional),"{:.2f}".format(intellectual))


