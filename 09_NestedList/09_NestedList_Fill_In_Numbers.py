def pattern1(nrows, ncols): #nrows  0,ncols  0
    k = 1
    c = []
    temp = []
    for i in range(nrows):
        for j in range(ncols):
            temp.append(k)
            k+=1
        c.append(temp)
        temp = []
    return c
def pattern2(nrows, ncols): #nrows  0,ncols  0
    k = 1
    c = []
    temp = []
    add = nrows
    for i in range(1,nrows+1):
        k = i
        for j in range(0,ncols):
            temp.append(k)
            k+= add
            print(k)
        c.append(temp)
        temp = []
    return c
            
            
def pattern3(N): #N  0
    start = 0
    l = []
    for i in range(N):
        row = [j for j in range(start+1,start+1+N-i)]
        start = row[-1]
        if len(row) < N :
            row = [0]*(N-len(row)) + row
        l.append(row)
    return l
        
            
        
        
            
            
# defpattern4(N): #N  0
# defpattern5(N): #N  0
# defpattern6(N): #N  0
# exec(input().strip())
print(pattern3(4))