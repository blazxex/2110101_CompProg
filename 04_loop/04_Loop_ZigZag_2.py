y = input().split()
# for row 0
red_zig = int(y[0])
blue_zig = int(y[1])
red_zag = int(y[1])
blue_zag = int(y[0])
i=0

while y[0]!= 'Zig-Zag' and y[0]!= 'Zag-Zig':
    if i%2==0:
        red_zig = min(red_zig,int(y[0]))
        blue_zig = max(blue_zig,int(y[1]))
        red_zag = min(red_zag,int(y[1]))
        blue_zag = max(blue_zag,int(y[0]))
    elif i%2==1:
        red_zig = min(red_zig,int(y[1]))
        blue_zig = max(blue_zig,int(y[0]))
        red_zag = min(red_zag,int(y[0]))
        blue_zag = max(blue_zag,int(y[1]))
    y = input().split()
    i+=1
    #print(red_zag,blue_zag)
    

if y[0]=='Zig-Zag':
    print(red_zig,blue_zig)
elif y[0]=='Zag-Zig':
    print(red_zag,blue_zag)
    