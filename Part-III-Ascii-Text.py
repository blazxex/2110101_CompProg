file_name = input().strip()
cmd = input().strip()
fn = open(file_name,'r')
lin = fn.readlines()
lin = [x.strip() for x in lin]
fn.close()
l_strip = []
r_strip = []
for txt in lin:
    for i,a in enumerate(txt):
        if a!= '.':
            l_strip.append(i)
            break
    for i,a in enumerate(txt[::-1]):
        if a!= '.':
            r_strip.append(len(txt)-i)
            break
if cmd =='LSTRIP':
    for txt in lin:
        print(txt[min(l_strip):])
elif cmd =='RSTRIP':
    for txt in lin:
        print(txt[:max(r_strip)])
elif cmd == 'STRIP':
    for txt in lin:
        print(txt[min(l_strip):max(r_strip)])
elif cmd == 'STRIP_ALL':
    is_dot = []
    for i,txt in enumerate(lin):
        new_line = txt[min(l_strip):max(r_strip)]
        for j,a in enumerate(new_line):
            if a== '.':
                if len(is_dot)< i+1:
                    is_dot.append(set([j]))
                else:
                    is_dot[i] = is_dot[i] | set([j])
    itc = is_dot[1].intersection(is_dot[0])
    for st in is_dot:
        itc = itc.intersection(st)
    delt = sorted(list(itc))
    
    for i,txt in enumerate(lin):
        new_line = txt[min(l_strip):max(r_strip)]
        for j,a in enumerate(new_line):
            if j not in delt:
                print(a,end='')
        print()
else: 
  print('Invalid commamd')