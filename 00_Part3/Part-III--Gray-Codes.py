import math
def gray(n,k):
    x = ['0','1']
    for i in range(1,n):
        y = x + x[::-1]
        i = int(len(y)/2)
        x = []
        for j in range(i):
            x.append('0'+str(y[j]))
        for k in range(i,len(y)):
            x.append('1'+str(y[k]))
    return x

n = int(input())
k = int(input())
out = ''
status = True
if n<=0 and k< 1:
    print('Invalid n and k')
    status = False
else:
    if n <= 0:
        print('Invalid n')
        status = False
    if k < 1:
        print("Invalid k")
        status = False
if status:
    for i in range(1,k+1):
        m = n
        if len(str(i))!=1:
            m = m-len(str(i))+1
        if i == k:
            m = m-1
        out += str(i) + '-'*m
        
    print(out)
    code = gray(n,k)
    a = 0
    b = k
    for z in range(math.ceil(len(code)/k)):
        print(','.join(code[a:b]))
        a+=k
        b+=k
    

    