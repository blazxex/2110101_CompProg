def add_poly(p1, p2):
    op = []
    new_p1 = p1.copy()
    new_p2 = p2.copy()
    for (a,b) in p1:
        for (c,d) in p2:
            if b == d:
                op.append((a+c,b))
                new_p1.remove((a,b))
                new_p2.remove((c,d))
    op = op+new_p1+new_p2
    op = sorted(op , key=lambda x:x[1],reverse=True)
    op = [(x,y) for (x,y) in op if x!= 0]
    return op
                
def mult_poly(p1, p2):
    mult= []
    new_mult = []
    for (a,b) in p1:
        for (c,d) in p2:
            mult.append((a*c,b+d))
    mult = sorted(mult , key=lambda x:x[1],reverse=True)
    for i in range(0,len(mult)-1):
        if mult[i][1] == mult[i+1][1]:
            new_mult.append((mult[i][0]+mult[i+1][0],mult[i][1]))
            
        else:
            new_mult.append((mult[i][0],mult[i][1]))
            if len(mult)-2 ==i:
                new_mult.append((mult[i+1][0],mult[i+1][1]))
         
    return add_poly(new_mult[1:])
     
for i in range(3):
  exec(input().strip())