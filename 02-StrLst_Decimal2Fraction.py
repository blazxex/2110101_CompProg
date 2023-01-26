import math
x=input().split(',')

b = int('0'+x[1])

frac =int(b+x[2])

bot  = ('9'*(len(x[1])-1)+'0'*(len(x[b])-1))
print(bot)
top = (int(frac)-b)*int(bot)
mo = math.gcd(top,int(bot))
print(top//mo,'/',int(bot)//mo)

# top = int(b)-int(c)






