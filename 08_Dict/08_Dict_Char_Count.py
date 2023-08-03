import string
text = input().strip().lower()
new = ''
for x in text:
    if x not in string.punctuation and x != ' ' and not('0'<=x<='9'):
        new+=x
sum ={}
for x in new:
    if x not in sum:
        sum[x] = 1
    else:
        sum[x] +=1
z = []
for x in sum:
    z.append([-1*sum[x],x])
z.sort()
for a,b in z:
    print(b,'->',-1*a)
    

