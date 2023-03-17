pizza = {
    'PZ871':265.25,
    'PZ953':246.50,
    'Z1983':256.50,
    'Z2853':272.50,
    'LC673':309.25
}

order_cal= {}
num = int(input())
for i in range(num):
    order = input().split(',')
    customer_id = order[0]
    for i in range(1,len(order[1:]),2):
        if customer_id not in order_cal:
            order_cal[customer_id] = pizza[order[i]]*int(order[i+1])
        else:
            order_cal[customer_id]+= pizza[order[i]]*int(order[i+1])
cal_list  = sorted([[x,y] for (x,y) in order_cal.items()])
for a,b in cal_list:
    print(a,'->',round(b,2))
    
    
