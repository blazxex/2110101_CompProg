file_name = input()
old_word = input()
new_word = input()
len_repWord = len(old_word)

fn = open(file_name,'r')
line = fn.readlines()

for path in line:
    newword_index = []
    i=0
    count = 0
    new_string=''
    
    if path[0]!='/' and path[len_repWord]=='/':
        for k in range(len_repWord):
            if path[k].lower()==old_word[k].lower():
                    count+=1
                    # print('ssd')
            elif  old_word[k].lower()=='?':
                count+=1
            if count == len_repWord:
                newword_index.append([0,len_repWord])
                count = 0
    
    
    while i < len(path):
        
        if path[i]=='/' and path[i+len_repWord+1]=='/' :  #find / word  /
            # print('ss')
            for j in range(len_repWord): # loop to check word with old word
                # print(path[i+j+1].lower(),old_word[j].lower())
                print(i,j)
                if path[i+j+1].lower()==old_word[j].lower():
                    count+=1
                    # print('ssd')
                elif  old_word[j].lower()=='?':
                    count+=1
            # print(count)
            if count == len_repWord:
                newword_index.append([i+1,i+len_repWord+1])
                count = 0
        i+=1
    z = 0
    # print(newword_index)
    for x,y in newword_index:
        new_string+= str(path[z:x])+new_word
        z = y
    # print(z)
    new_string+= str(path[z:])
    print(new_string,end='')