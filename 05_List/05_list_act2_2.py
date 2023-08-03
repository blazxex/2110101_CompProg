num = input().split()
num = [float(x) for x in num]
add_num = [0]*(2*len(num)-1)
i= 0 
for x in num:
    add_num[i] = x
    i+=2
for y in range(1,len(add_num)-1,2):
    add_num[y] = (add_num[y+1]+add_num[y-1])/2
print(add_num)
    

