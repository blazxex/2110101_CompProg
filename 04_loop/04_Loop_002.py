d = [int(e) for e in input().split()]
p = d[-1:]
i=-1
j=0
n = len(d)
while j< n-1:
    if int(d[j]) <= int(p[0]):
       i+= 1
       d[i],d[j]=d[j],d[i]
    j+=1
d[i+1],d[n-1]= d[n-1],d[i+1]
print(d)