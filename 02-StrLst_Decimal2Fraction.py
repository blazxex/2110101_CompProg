import math
x=input().split(',')

a = x[0]  #จนเต็ม
b= '0'+x[1] #ไม่ซ้ำ
c = b+x[2] #ซ้ำ

top = int(b+x[2])-int(b)
bot = int('9'*len(x[2])+'0'*(len(b)-1))
top2 = top + int(a)*bot
div = math.gcd(top2,bot)
st = top2//div
nd = bot//div
print(st,'/',nd)