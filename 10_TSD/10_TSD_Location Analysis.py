city_id = {}
id_city = {}
id_order = []
for i in range(int(input())):
    id,city = input().split(':')
    id_order.append(id)
    id_city[id] = city.split(',')
    for c in city.split(','):
        x = c.strip()
        if x not in city_id:
            city_id[x] = [id.strip()]
        else:
            city_id[x].append(id.strip())
search_id = input().strip()
hb_city = id_city[search_id]
id_total = set()
for x in hb_city:
    id_total = id_total | set(city_id[x.strip()])
hb = id_total-set([search_id])
if len(hb) == 0:
    print('Not Found')
else:
    out =[]
    for z in hb:
       out.append([id_order.index(z),z])
    out.sort()
    for j in out:
        print(j[1]) 
    
# print(hb_city)
# print(city_id)

# 6
# 51234621: A, B, D, E, F 
# 427613829: B, D, G, H, I 
# 38216542: Z, B, D, J 
# 423212822: AA, B1, C3, D 
# 4126548: J, Z3 
# 98871973331: Q, M, N 
# 423212822




