student = {}   #{name : {group: ,grade: , major}}
for i in range(int(input())):
    line = input().split()
    name = line[0]
    group = line[1]
    grade = line[2]
    major = line[3]
    student[name] = {'group':group,'grade':grade,'major':major}
srt = input().split()
srt_check = [0,0,0]
for x in srt:
    if '0'<= 'x'<='1000':
        srt_check[1] = x 
    if len(x) == 2:
        srt_check[2] = x 
    if len(x) == 1:
        srt_check[0] = x 
for (std,detail) in student.items():
    if detail['group'] == srt_check[0] and detail['grade'] == srt_check[1] and detail['major'] == srt_check[2]:
        print(" ".join([std,detail]))

    
        

    