def str2RLE(text):
    n=1
    for i in range(len(text)-1):
        if text[i]!=text[i+1]:
            print(text[i],n,end=' ')
            n=1
        else:
            n+=1
    pass
def RLE2str(text):
    for i in range(0,len(text),2):
        print(str(text[i])*int(text[i+1]),end='')



command = input()
if command =='str2RLE':
    str2RLE(input()+' ')
elif command =='RLE2str':
    x = input().split()
    RLE2str(x)
else:
    print("Error")

