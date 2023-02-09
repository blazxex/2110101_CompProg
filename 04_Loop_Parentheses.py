x = input()
before =['(','[',')',']']
after = ['[','(',']',')']
for i in range(len(x)):
    if x[i] in before:
        print(after[before.index(x[i])],end='')
    else:
        print(x[i],end="")
# print(x)