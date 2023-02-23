a = input()
b=''
for x in a:
    if x=='+' or x=='-':
        b+=' '+x
    else: b+=x
c = b.split()
sum=0
for d in c:
    sum+=int(d)
print(sum)
