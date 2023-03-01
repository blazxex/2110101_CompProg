

s=''
text = input().strip()

for j,x in enumerate(text):
    for i,y in enumerate(x):
        if ord('0')<=ord(y)<=ord('9')or ord('A')<=ord(y)<=ord('z'):
            s+=y
        else: s+= ' '
s = s.split()
for i,a in enumerate(s):
    if i ==0:
        print(a.lower(),end='')
    else:
        print(a[0].upper()+a[1:].lower(),end='')
