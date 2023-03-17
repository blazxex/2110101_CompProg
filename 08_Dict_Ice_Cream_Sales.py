n = int(input())
stock = {}
for i in range(n):
    x,y = input().split()
    stock[x] = int(y)
num = int(input())
sell = {}
total_sales = 0
top_sell = []
for j in range(num):
    a,b =input().split()
    if a in stock:
        total_sales+=stock[a]*int(b)
        if a not in sell:
            sell[a]=int(b)*stock[a]
        else:
            sell[a]+=int(b)*stock[a]
top = 0
if len(sell) == 0:
    print('No ice cream sales')
else:
    for x in sell:
        if sell[x]>top:
            top = sell[x]
    for y in sell:
        if sell[y]==top:
            top_sell.append(y)
    print('Total ice cream sales:',float(total_sales))
    print('Top sales:',', '.join(sorted(top_sell)))
    
    
    


# Magnum 5
# Magnum 5
# Cookie 20
# MamaTomYum 3
# Cornetto 20
# AsianDelight 1