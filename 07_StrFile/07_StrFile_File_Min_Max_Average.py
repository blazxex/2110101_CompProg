name,year = input().split()
fn = open('data.txt','r')
line = fn.readlines()

num= []
for x in line:
    a,b=x.split()
    if a[:2] == year[-2:]:
        num.append(float(b))
if len(num)!= 0:
    print(min(num),max(num),sum(num)/len(num))
else:
    print('No data')
fn.close()

