num = int(input()) 
one = []
two = []
for i in range(1,num+1):
    x,y =input().split()
    if i%2==1:
        one.append(int(x))
        two.append(int(y))
    if i%2==0:
        one.append(int(y))
        two.append(int(x))
        
command = input()
if command=='Zig-Zag':
    print(min(one),max(two))
else:
    print(min(two),max(one))

  
    
    
    