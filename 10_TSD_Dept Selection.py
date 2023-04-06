major = {}
student = []
student_major = []
for i in range(int(input())):
    text = input().split()
    major[text[0]] = int(text[1])
for j in range(int(input())):
    std = input().split()
    student.append([std[1],std[0],std[2:]])
student = sorted(student,key = lambda x:(-float(x[0]) ,float(x[1])))
for x in student:
    for y in x[2]:
        if major[y] >0:
            student_major.append([x[1],y])
            major[y] -=1
            break
for z in sorted(student_major):
    print(" ".join(z))

    
