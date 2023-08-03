def index_of(grades,ID):
    y=9
    for [x,y] in grades:
        if str(x)==str(ID):
            return (grades.index([x,y]))
    if y!=1:
        return -1
        
def upgrade(grades,IDs):
    grade =['A','B+','B','C+','C','D+','D','F']
    for [x,y] in grades:
        if x in IDs:
            if y !='A':
                grades[grades.index([x,y])][1]= grade[grade.index(y)-1]      
    grades.sort()

# grades = [['222','B'], ['111','A'], ['444','D'], ['33','C+']]
# print( index_of( grades, '444' ) ) 
# print( index_of( grades, '555' ) )

exec(input())
exec(input())
exec(input())
