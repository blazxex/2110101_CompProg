a =input()
b =input()
c =input()
d =input()
e =input()
med=0
if a>b:
    a,b=b,a
if c>d:
    c,d=d,c
if a>c:
    b,d=d,b
    c=a
a=e
if a>b:
    a,b=b,a
if c>a:
    b,d=d,b
    a=c
if a>d:
    med = d
else:
    med =a
print(med)
