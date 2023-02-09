x=0
sum=0
count = 0
while True:
    num = input()
    if num =='q':
        break
    sum+=float(num)
    count+=1
if count == 0:
    print('No Data')  
else:
    print(round(sum/count,2))