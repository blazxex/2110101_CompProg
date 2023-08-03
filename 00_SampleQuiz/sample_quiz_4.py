def match(text,pattern):
    if len(text)!=len(pattern):
        return False
    for i in range(len(text)):
        if text[i].lower()!=pattern[i] and pattern[i]!= '?':
            return False
    return True
def rename(path,pattern,new_word):
    idx_1 = 0
    out = ''
    while True:
        idx_2 = path.find('/',idx_1)
        if idx_2 ==-1:
            break
        check = path[idx_1:idx_2]
        if match(check,pattern):
            out+=new_word + '/'
        else:
            out+= check + '/'
        idx_1 = idx_2+1
    out += path[idx_1:]
    return out  
file_name = input()
pattern = input()
new_word = input()

f = open(file_name,'r')
for line in f:
    line = line.strip()
    print(rename(line,pattern,new_word))
f.close()