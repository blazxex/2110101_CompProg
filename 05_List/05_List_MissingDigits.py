text = input()
num = [0]*10
missing = []
# strNum = [str(x) for x in num]
for tt in text:
    if '0'<= tt <='9':
        num[int(tt)]+=1
i = 0
for k in num:
    if k == 0:
        missing.append(str(i))
    i+=1
y = ','.join(missing)
if len(y)!= 0:
    print(y)
else: print("None")
        