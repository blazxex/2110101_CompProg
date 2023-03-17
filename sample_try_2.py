# file_name = input()
# old_word = input()
# new_word = input()
file_name = 'data.txt'
old_word = 'Do?k??'
new_word = 'JAZZZZ'
len_old = len(old_word)

fn = open(file_name,'r')
line = fn.readlines()
for path in line:
    s = '' 
    id_p = 0
    add_slsh = 0
    if path[0]!='/':
        path = '/'+path
        add_slsh = 1
    while id_p < len(path): # loop letter in path
        if path[id_p]== '/' :
            count = 0# check is it folder
            for i in range(len_old): # loop in old_word
                    if path[id_p+i+1 ].lower() == old_word[i].lower(): # check if pattern == text
                        count+=1 # if equal += 1
                    elif old_word[i] == '?': #+=1 
                        count+=1
                    if count>4:
                        count = 0  
                    if count == len_old and path[id_p+i+2]=='/':
                        # print('sddsd')
                        s+= '/'+new_word
                        id_p +=len_old+1
                        count=0
        s+= path[id_p]
        id_p+=1
    if add_slsh ==1:
        print(s[1:].rstrip())
    else:
        print(s.rstrip())
fn.close()
                
