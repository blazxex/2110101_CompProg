real = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']

n = int(input())
for i in range(n):
    name = input()
    if name in real:
        print(nick[real.index(name)])
    elif name in nick:
        print(real[nick.index(name)])
    else: print('Not found')