a = input()
x=input()
b = a[1:len(a)-1]
y = x[1:len(x)-1]
c= b.split(',')
z = y.split(',')
sum = []
aToFlt = [float(x) for x in c]
bToFlt= [float(x) for x in z]

for i in range(3):
    sum.append((float(c[i])+float(z[i])))
print(aToFlt,'+',bToFlt,'=',sum)




