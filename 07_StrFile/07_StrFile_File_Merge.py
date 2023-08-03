name_1,name_2 = input().split()
f1 = open(name_1,'r')
f2 = open(name_2,'r')
f1_line = f1.readlines()
f2_line = f2.readlines()
sum = f1_line+f2_line

sum = [x.split() for x in sum]
sum = [[a[-2:],[a,b]] for a,b in sum]
sum.sort()
for x in sum:
    print(x[1][0],x[1][1])


f1.close()
f2.close()
