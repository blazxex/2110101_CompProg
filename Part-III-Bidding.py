prod_bidder = {}
sum_winning = {} # {id:[[price,prod]]}
for i in range(1,int(input())+1):
    bid = input().split()
    if bid[0] == 'B':
        id = bid[1]
        if id not in sum_winning:
            sum_winning[id] = []
        prod = bid[2]
        price = int(bid[3])
        if prod not in prod_bidder:
            prod_bidder[prod] = {id:(price,i)}
        else:
            prod_bidder[prod].update({id:(price,i)})
    if bid[0] == 'W':
        id = bid[1]
        prod = bid[2]
        if prod in prod_bidder:
            if id in prod_bidder[prod]:
                prod_bidder[prod].pop(id)
winning = {a:'' for a in prod_bidder.keys()}
for x in prod_bidder:
    temp = []
    temp = sorted([[price,i,auc] for (auc,(price,i)) in prod_bidder[x].items()],key=lambda x:(-x[0],x[1]))
    if temp != []:
        winning[x] = [temp[0][2],temp[0][0]]   # id,price
    
for prod in winning:
    if winning[prod]!= '':
        id = winning[prod][0]
        price  = winning[prod][1]
        if id not in sum_winning:
            sum_winning[id] = [prod,price]
        else:
            sum_winning[id].append([prod,price])
out = []
for (id,got) in sum_winning.items():
    if len(got)==0:
        out.append(id+': $0')
    else:
        sum_price = sum([int(x[1]) for x in got])
        sum_prod =  [y[0] for y in got]
        out.append(id+": "+'$'+str(sum_price)+' -> '+' '.join(sorted(sum_prod)))
out.sort()
for z in out:
    print(z)
    
