num = str(input())
fstNum = num[3]+num[10]+num[17]+num[24]+num[31]
sndNum = num[7]+num[12]+num[17]+num[22]+num[27]
sumNum = str(int(fstNum)+int(sndNum)+10000)
threeDigit = sumNum[-4:-1]
lastDigit = ((int(threeDigit[0])+int(threeDigit[1])+int(threeDigit[2]))%10)+1
alphabet = ['A','B','C','D','E','F','G','H','I','J']
print(threeDigit+alphabet[lastDigit-1])
