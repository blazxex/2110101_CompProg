n = int(input())
li = []
i= 0 
for i in range(n):
    num = int(input())
    if i%2==0:
        li.append(num)
    else:
        li.insert(0,num)
set_2 = [int(x) for x in  input().split()]
if i==0:
    i=1
for num in set_2:
    i+=1
    if i%2==0:
        li.append(num)
    else:
        li.insert(0,num)
        
num = int(input())
while num!= -1:
    i+=1
    if i%2==0:
        li.append(num)
    else:
        li.insert(0,num)
    num = int(input())
print(li)
    