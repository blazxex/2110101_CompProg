member_count = {}
ota_oshi = {}
member_oshicount = {}

while True:
    vote = input().strip().split()
    if len(vote) == 1:
        command = int(vote[0])
        break
    ota = vote[0].strip()
    member = vote[1].strip()
    ticket = int(vote[2].strip())
    
    if member not in member_count:
        member_count[member] = [ticket,[ota]]
        member_oshicount[member] = 0
    else:
        member_count[member][0] += ticket
        member_count[member][1].append(ota)
    
    if ota not in ota_oshi:
        ota_oshi[ota] = {member:ticket}
    else:
        if member not in ota_oshi[ota]:
            ota_oshi[ota].update( {member:ticket})
        else:
            ota_oshi[ota][member]+=ticket
if command ==1 :
    out = []
    for name in member_count:
        out.append([member_count[name][0],name])
    out = [z[1] for z in sorted(out ,key=lambda x:(-int(x[0]),x[1]))]
    print(', '.join(out[:3]))
elif command ==2:
    out = []
    for name in member_count:
        out.append([len(set(member_count[name][1])),name])
    out = [z[1] for z in sorted(out ,key=lambda x:(-int(x[0]),x[1]))]
    print(', '.join(out[:3]))
elif command == 3:
    out = []
    temp = []
    for name in ota_oshi:
        temp = [[cn,nm] for (nm,cn) in ota_oshi[name].items()]
        temp = sorted(temp, key=lambda x:(-x[0],x[1]))
        member_oshi = temp[0][1]
        if member_oshi not in member_oshicount:
            member_oshicount[member_oshi] = 1
        else:
             member_oshicount[member_oshi] += 1
    out = [[ct,nm] for (nm,ct) in member_oshicount.items()]
    temp = [z[1] for z in sorted(out ,key=lambda x:(-int(x[0]),x[1]))]
    print(', '.join(temp[:3]))
    
        
    
# SOMCHAI CHERPRANG 10 
# SOMCHAI NATHERINE 5 
# PRABHAS JENNIS 3 
# SOMCHAI CHERPRANG 4 
# DUANGDAO TURTLE 1 
# EKAPOL TURTLE 1
# SETHA TURTLE 1 
# CHAIRAT TURTLE 1 
# JENNIS JENNIS 10 
# PRABHAS JANE 8 
# MANA CHERPRANG 2 
# MANEE CHERPRANG 1 
# CHUJAI TURTLE 1
# PITI JENNIS 1
# PITI JANE 1
# VEERA CHERPRANG 1