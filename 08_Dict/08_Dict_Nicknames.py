def find_name(search,name,name_2):
    if search in name:
        return name[search]
    elif search in name_2:
        return name_2[search]
    else: return 'Not found'
    


num_in = int(input())
name ={}
name_2 ={}
for i in range(num_in):
    Realname,nickname = input().split()
    name[Realname] = nickname
    name_2[nickname] = Realname
    
num_2 = int(input())
for j in range(num_2):
    search_name = input().strip()
    print(find_name(search_name,name,name_2))