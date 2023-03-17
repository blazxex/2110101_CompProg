filename = input()
pattern  = input().lower()
new_name = input()
f = open(filename)
for line in f :
    line = line.strip()
    print(rename(line,pattern,new_name))
pattern = 'te??'
line = 'c:/temp/Temp/TeMM/doc/FO'
k1 = 0
while True:
    k2 = line.find('/',k1)
    out = ''
    if k2 == -1: break
    folder_name = line[k1:k2]
    if match(folder_name,pattern):
        out += new_name
    else:
        out += folder_name
    k1 = k2+1
    

