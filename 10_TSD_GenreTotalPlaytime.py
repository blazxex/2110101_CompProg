genre = {}
for i in range(int(input())):
    line = input().split(',')
    line = [x.strip() for x in line]
    if line[2] not in genre:
        time = line[3].split(':')
        
        genre[line[2]] = float(time[0])*60 +float(time[1])
    else:
        time = line[3].split(':')
        genre[line[2]] += float(time[0])*60 +float(time[1])
genre_list = [[t,g] for (g,t) in genre.items()]
genre_list.sort(reverse=True)
for x in genre_list[:3]:
    min = int(float(x[0])//60)
    s = int(x[0])-min*60
    if s <10:
        s = '0'+str(s)
    print(x[1],'-->',str(min)+':'+str(s))
    
