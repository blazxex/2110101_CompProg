f = open("out.txt",'w')

for i in range(1,6):
    x = i**2
    f.write(str(x)+'\n')
f.close()

