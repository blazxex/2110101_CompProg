q = list()
n_order = int(input())
count=0
total_time=0
for i in range(n_order):
    order = input().split()
    if order[0]=='reset':
        n = int(order[1])
        que = n-1
    elif order[0]=='new':
        print('ticket',n)
        q.append([n,order[1]])
        n+=1
    elif order[0]=='next':
        que+=1
        print('call',que)
    elif order[0]=='order':
        for [x,y] in q:
            if x == que:
                time = int(order[1])-int(y)
                count+=1
        total_time+=time
        print('qtime',que,time)
    elif order[0]=='avg_qtime':
        print('avg_qtime',total_time/count)
        
    