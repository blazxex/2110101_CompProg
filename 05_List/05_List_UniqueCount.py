num = [int(x) for x in input().split()]
li = []
num.sort()
check = num[0]
for i in range(1,len(num)):
    if check!=num[i]:
        li.append(check)
        check = num[i]
li.append(check)
print(len(li))
print(li[:10])
