def distance1(x1, y1, x2, y2): 
    return ((x2-x1)**2+(y2-y1)**2)**0.5
    
    
def distance2(p1, p2):
    return distance1(p1[0],p1[1],p2[0],p2[1])
    

def distance3(c1, c2):
    dis_center = distance2(c1[0:2],c2[0:2])
    r = c1[2]+c2[2]
    if dis_center<=r:
        return dis_center,True
    else:
        
        return dis_center,False

def perimeter(points):
    sum=0
    for i in range(len(points)-1):
        sum+= distance2(points[i],points[i+1])
    sum+=distance2(points[0],points[len(points)-1])
    return sum
        

print(distance3([1,2,0.3],[1.5,3.2,1.0]))