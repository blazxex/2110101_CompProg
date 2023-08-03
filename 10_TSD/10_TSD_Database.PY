course = input().strip()
teacher = input().strip()
data = input().strip()
fn = open(course,'r')
fn2 = open(teacher,'r')
fn3 = open(data,'r')
course_s = {}
teacher_s ={}
for line in fn:
    n,t = line.strip().split(',')
    course_s[n] = t
for line2 in fn2:
    n,t = line2.strip().split(',')
    teacher_s[n] = t

for line3 in fn3:
    c,t = line3.strip().split(',')
    try:
        print(course_s[c]+','+teacher_s[t])
    except:
        print('record error')
fn.close()
fn2.close()
fn3.close()


