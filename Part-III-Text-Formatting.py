#-------------------------------------.
# Q4: Text Formatting
#----------------------------------------
fname = '101.txt'
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1)  # เพิ่มรอบละ 9 ขีด ตามด้วยตัวเลข
if len(ruler) < k : 
    ruler += '-'*(k-len(ruler))            # เพิ่มที่เหลือ (ถ้ามี)
print(ruler)

fn = open(fname,'r')
line = fn.readlines()
line = '.'.join([x.strip() for x in line])
a= 0 
b = k
i = 1
for ltr in line:
    
    if i<= k:
        
        
        if i==k and ltr =='.':
            pass
        else:
            print(ltr,end='')
        i+=1
        
                
    else:
        print()
        i = 1
        if ltr == '.':
            i=1
            pass
        else:print(ltr,end='')