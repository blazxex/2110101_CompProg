station = {}
while True:
    stt = input().split()
    if len(stt) == 1:
        break
    if stt[0] not in station:
        station[stt[0]] = [stt[1]]
    else:
        station[stt[0]].append(stt[1])
    if stt[1] not in station:
        station[stt[1]] = [stt[0]]
    else:
        station[stt[1]].append(stt[0])

un = set([stt[0]])
if stt[0] in station:
    un = un | set(station[stt[0]])
    for x in station[str(stt[0])]:
        un = un | set(station[x])
for stat in sorted(un):
    print(stat)

