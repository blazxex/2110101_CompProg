n = int(input())
li = []
for i in range(n):
    p = input().split()
    x = float(p[0])
    y=float(p[1])
    li.append([(x**2+y**2)**0.5,str(i+1),str(x),str(y)])
li.sort()
co = li[2]
print('#'+co[1]+':','('+co[2]+',',co[3]+')')