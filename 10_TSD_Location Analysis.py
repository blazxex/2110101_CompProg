city_id = {}
id_city = {}
for i in range(int(input())):
    id,city = input().split(':')
    id_city[id] = city.split()
    for c in city.split(','):
        x = c.strip()
        if x not in city_id:
            city_id[x] = [id.strip()]
        else:
            city_id[x].append(id.strip())
search_id = input().strip()
hb_city = id_city[search_id]
for a in hb_city:
    for b in city_id[a]:
        if b != search_id:
            print(b)






