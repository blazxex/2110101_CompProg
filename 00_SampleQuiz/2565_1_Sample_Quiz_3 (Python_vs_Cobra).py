party_member = {}
party_order = []
party_vote = {}
party_finalize = {}
mem_party = {}
mem_vote = []  #[mem,vote]
party_cobra = {}
for i in range(int(input())):
    party = input().strip()
    party_order.append(party)
    party_cobra[party] = []
    party_member[party] = set()  # party_name: set of member of house
    party_vote[party] = {'Y':0,'N':0,'X':0}
for j in range(int(input())):
    member , owner = input().split()
    mem_party[member] = owner
    party_member[owner] = party_member[owner] | (set([member]))
for k in range(int(input())):
    mem , vote = input().split()
    mem = mem.strip()
    vote = vote.strip()
    mem_vote.append([mem,vote])
    for name in party_member:
        if mem in party_member[name]:
            party_vote[name][vote]+=1
for vt in party_vote:
    finalize = [[party_vote[vt]['Y'],'Y'],[party_vote[vt]['N'],'N'],[party_vote[vt]['X'],'X']]
    finalize.sort(reverse=True)
    if finalize[0][0] ==0:
        party_finalize[vt] = 'Inconclusive'
        party_cobra[vt] = ['Inconclusive']
    elif finalize[0][0] == finalize[1][0]:
        party_finalize[vt] = 'Inconclusive'
        party_cobra[vt] = ['Inconclusive']
    else:
        party_finalize[vt] = finalize[0][1]
for [mem,vote] in mem_vote:
    if party_finalize[mem_party[mem]] != vote and party_finalize[mem_party[mem]]!='Inconclusive':
        party_cobra[mem_party[mem]].append(mem)
for pt in party_order:
    if party_cobra[pt] == []:
        print(pt)
        print('No cobra')
    else:
        print(pt)
        print(', '.join(sorted(party_cobra[pt])))
    




        