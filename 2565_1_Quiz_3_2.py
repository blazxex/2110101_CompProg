n,m,k = input().split()
name_fac = {}
guest_fac ={}
for i in range(int(n)):
    name,fac = input().split()
    name_fac[name] = fac
for j in range(int(m)):
    txt = input().split()
    guest = txt[0]
    guest_fac[guest] = set()
    for std in txt[1:]:
        guest_fac[guest] = guest_fac[guest] | (set([name_fac[std]]))
for k in range(int(k)):
    search = input().split()
    itc = guest_fac[search[0]]
    for x in search:
        itc = itc.intersection(guest_fac[x])
    itc = list(itc)
    if len(itc) == 0:
        
        print('None')
    else:
        print(' '.join(sorted(itc)))
        # find intersection  and return in order 
        
        
        
# 8 3 2
# Luffy faculty_a
# Nami faculty_a
# Sanji faculty_b
# Zoro faculty_c
# Robin faculty_c
# Chopper faculty_a
# Brook faculty_c
# Franky faculty_b
# Eren Nami Chopper Brook
# Anya Sanji Luffy
# Yaiba Franky
# Eren Anya
# Anya Eren Yaiba


# 8 2 1
# Luffy faculty_a
# Nami faculty_a
# Sanji faculty_b
# Zoro fac_c
# Robin fac_c
# Chopper faculty_a
# Brook fac_c
# Franky faculty_b
# Shinji Sanji Chopper
# Amuro Zoro Sanji Nami
# Amuro Shinji