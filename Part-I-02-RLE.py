command = input()

RLE = []
count=1
if command == 'str2RLE':
    code = input()
    for i in range(len(code)-1):
        if code[i]==code[i+1]:
            count+=1
        else:
            RLE.append(code[i])
            RLE.append(str(count))
            count=1
        
    print(' '.join(RLE))
elif command == 'RLE2str':
    code = input().splir()
    for j in range(0,len(code),2):
        print(code[j]*int(code[j+1]),end='')
else:
    print('Error')
            
        
            
