def match(x,p):
    if len(x) != len(p):
        return False
    for i in range(len(x)):
        if p[i]!= '?' and x[i].lower()!=p[i]:
            return False
    return True

def rename(line,pattern,new_word):
    k1 = 0
    out = ''
    while True:
        k2 = line.find('/',k1)
        if k2==-1:
            break
        folder_name = line [k1:k2]
        if match(folder_name,pattern):
            out+= new_word  + '/'
        else:
            out += folder_name +'/'
        k1 = k2+1
    out+= line[k1:]
    return out

file_name = 'data.txt'
pattern = 'T?m?'.lower()
new_word = 'Python'  

f = open(file_name)
for line in f:
    line = line.strip()
    print(rename(line,pattern,new_word))
f.close()
