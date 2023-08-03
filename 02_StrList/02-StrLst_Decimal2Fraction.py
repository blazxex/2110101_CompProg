# i =1
# x = input().split()
# red=int(x[0])
# blue = int(x[1])
# while True:
#     x = input().split()
#     if x[0] == 'Zig-Zag':
#         break
#     if i%2==1:
#         red = min(red,int(x[0]))
#         blue = max(blue,int(x[1]))
#     elif i%2==0:
#         red = min(int(x[1]),red)
#         blue = max(int(x[0]),blue)
# print(red,blue)
# print(blue,red)
x=[]
while True:
    y = input().split()
    if y[0]=='Zig-Zag' or y[0]=='Zag-Zig':
        break
    x = x+[[int(a),int(b)] for a,b in y]
    

