h = int(input())
for i in range(h-1):
    for j in range(h-1,i,-1):
        print('.',end='')
    print('*',end='')
    for k in range(0,2*i-1):
        print('.',end='')
    if i ==0:
        print()
        pass
    else:
        print('*')
for l in range(2*h-1):
    print('*',end='')
        