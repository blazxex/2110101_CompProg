ids =[]
grades =['A','B+','B','C+','C','D+','D','F']
id_grade =[]
x = input().split()
while x[0]!= 'q':
    ids.append(x[0])
    id_grade.append(x[1])
    x = input().split()
fix_grade = input().split()

for x in fix_grade:
    if x in ids:
        if id_grade[ids.index(x)]!='A':
            id_grade[ids.index(x)]= grades[grades.index(id_grade[ids.index(x)])-1]

srt =[]
for i in range(len(ids)):
    srt.append([ids[i],id_grade[i]])
srt.sort()
for j in range(len(srt)):
    print(srt[j][0],srt[j][1])

        
    

