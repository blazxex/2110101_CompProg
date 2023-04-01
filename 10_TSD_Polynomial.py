def add_poly(p1, p2):
    op = []
    new_p1 = p1.copy()
    new_p2 = p2.copy()
    for (a,b) in p1:
        for (c,d) in p2:
            print((a,b),(c,d))
            if b == d:
                op.append((a+c,b))
                new_p1.remove((a,b))
                new_p2.remove((c,d))
                print((a,b),(c,d))
    op = op+new_p1+new_p2
    op = sorted(op , key=lambda x:x[1],reverse=True)
    op = [(x,y) for (x,y) in op if x!= 0]
    return op
                
def mult_poly(p1, p2):
    for (a,b) in p1:
        for (b,c)

p1 = [(3,6),(2,4),(1,1),(-1,0)] 
p2 = [(3,4),(-1,1)] 
print(add_poly(p1, p2))