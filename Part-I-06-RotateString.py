def checkCode(str,num):
    count = 0
    for i in range(0,num-1):
        if len(str[i])!=len(str[i+1]):
            count+=1
    return count
    

ops = input().strip()
n = int(input())
text=[]
for i in range(0,n):
    code = input().strip()
    text.append(code)    
if checkCode(text,n)!=0:
    print('Invalid size')
else:
    if ops == '90':
        for k in range(len(code)):
            for j in range(n-1,-1,-1):
                print(text[j][k],end='')
            print()
    elif ops == 'flip':
        for k in range(n):
            for j in range(len(code)-1,-1,-1):
                print(text[k][j],end='')
            print()
    elif ops =='180':
        for k in range(n-1,-1,-1):
            for j in range(len(code)-1,-1,-1):
                print(text[k][j],end='')
            print()

            
    
