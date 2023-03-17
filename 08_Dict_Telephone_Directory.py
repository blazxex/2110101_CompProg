directory = {}
num = int(input())
for i in range(num):
    x = input().split()
    name,phone = ' '.join(x[:2]),x[-1]
    directory[name]=phone
    directory[phone] = name
time = int(input())
for j in range(time):
    search = input()
    if search in directory:
        print(search,'-->',directory[search])
    else:
        print(search,'-->','Not found')