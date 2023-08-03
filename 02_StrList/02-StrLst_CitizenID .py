id = input()
x=0
for i in range(12):
    x += int(id[i])*(13-i)
lastDigit = ((11-x%11))%10
for i in range(len(id)):
    print(id[i], end='')
    if i== 0 or i==4 or i==9 or i==11:
        print(" ",end='')

print(lastDigit)