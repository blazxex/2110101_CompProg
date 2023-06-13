fn = open('answer.txt','r')
fn2 = open('clean.txt','w')
line = fn.readlines()
for x in line:
    for z in x:
        if z =='#':
            break
        else:
            fn2.write(z)
    fn2.write('\n')