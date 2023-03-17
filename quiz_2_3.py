color_name = 'color.txt'
lyric_name = 'lyric.txt'
f1 = open(color_name,'r')
f2 = open(lyric_name,'r')

color = []
def match(line,color):
    id= 0 
    lower_line = line.lower()
    for x in color:
        id= lower_line.find(x)
        if id != -1:
            tag = "<"+x+'>'+line[id:id+len(x)]+"</>"
            line = line[:id]+tag + line[id+len(x):]
            lower_line = line.lower()
    return line

for line in f1:
    color+=line.split()
f1.close()
color = [cl.lower() for cl in color]

for line_2 in f2:
    print(match(line_2.rstrip(),color))
f2.close()

