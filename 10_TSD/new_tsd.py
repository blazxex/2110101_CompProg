major = {}
for i in range(int(input())):
    m,n = input().split()
    major[m] = int(n)
temp = []
for j in range(int(input())):
    txt = input().split()
    id = txt[0]
    grade = float(txt[1])
    select = txt[2:]
    temp.append([grade,id,select])
temp = sorted(temp,key=lambda x:(-x[0],x[1]))
out = []
for std in temp:
    id = std[1]
    mj = std[2]
    for x in mj:
        if major[x] > 0:
            out.append([id,x])
            major[x]-=1
            break
out.sort()
for z in out:
    print(' '.join(z))

# 5
# CP 1
# ME 2
# PE 1
# CHE 1
# MT 3
# 6
# 59301234521 23.6 PE CP MT CHE
# 59300799921 44.5 ME CP CHE PE
# 59300081621 37 PE CHE MT CP
# 59300653521 61.2 PE MT CP ME
# 59300002121 19.4 CHE CP ME CP
# 59300048721 7 ME CP CHE MT