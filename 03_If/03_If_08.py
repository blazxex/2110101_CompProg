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
d= int(input())
m= int(input())
y= int(input())-543
doy=0
for i in range(1,m):
    doy += checkMonth(i,y)

print(doy+d)
    
