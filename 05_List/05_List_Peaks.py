num = [int(x) for x in input().split()]
peak = 0
for i in range(1,len(num)-1):
    if num[i-1]<num[i] and num[i]>num[i+1]:
        peak+=1
print(peak)