n = int(input())
fruit_vitamin = []
fruit_list = []
for i in range(n):
    a = input().split()
    fruit_vitamin.append(a)
    fruit_list.append(a[0])
command = input().split()
if command[0] == 'show':
    for x in fruit_vitamin:
        print(' '.join(x))
elif command[0] == 'get':
    count = 0
    for i,x in enumerate(fruit_list):
        if x== command[1]:
            count = 1
            print(' '.join(fruit_vitamin[i]))
    if count == 0 :
        print(command[1],'not found')
elif command[0] == 'avg':
    id = int(command[1])
    sum = 0
    for x in fruit_vitamin:
        sum += float(x[id])
    print(round(sum/len(fruit_list),4))
elif command[0] == 'max':
    id = int(command[1])
    vitmin_sort = []
    for frt in fruit_vitamin:
        vitmin_sort.append([-1*float(frt[id]),frt[0]])
    vitmin_sort.sort()
    print(vitmin_sort[0][1],-1*float(vitmin_sort[0][0]))
elif command[0] == 'sort':
    id = int(command[1])
    sort_list = []
    for x in fruit_vitamin:
        sort_list.append([float(x[id]),x])
    sort_list.sort()
    name = [y[1][0] for y in sort_list]
    print(' '.join(name))
