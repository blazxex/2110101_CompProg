numStr = input()
numSplt = numStr.split()
sum=0
for i in range(len(numSplt)):
    sum += int(numSplt[i])
print(sum)