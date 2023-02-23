y = [float(x) for x in input().split()]
z =[0]*(2*len(y)-1)
i=0
for k in y:
        z[i]=float(k)
        i+=2
for j in range(1,len(z)-1,2):
    z[j] = (z[j-1]+z[j+1])/2
print(z)
    
