# Initialize variables
sport_lim = {}
sport_fac = {}
namep_sport = {}
output = []

# Read sports and their limits
while True:
    inp = input().strip()
    if inp == 'END':
        break
    sport, num = inp.split()
    sport_lim[sport] = int(num)
    sport_fac[sport] = {}

# Read people and the sports they play
while True:
    inp = input().strip()
    if inp == 'END':
        break
    name, fac, sports = inp.split(maxsplit=2)
    sports = set(s.strip() for s in sports.split(','))
    if name not in namep_sport:
        namep_sport[name] = (fac, sports)
    else:
        fac0, sports0 = namep_sport[name]
        if fac0 == fac:
            namep_sport[name] = (fac, sports0 | sports)
        else:
            name = name + fac
            namep_sport[name] = (fac, sports)

# Count the number of members for each sport and facility
for name, (fac, sports) in namep_sport.items():
    for sport in sports:
        if fac in sport_fac[sport]:
            sport_fac[sport][fac] += 1
        else:
            sport_fac[sport][fac] = 1

# Generate output
for sport in sorted(sport_lim):
    output.append(sport + ':')
    if sport in sport_fac:
        for fac, count in sorted(sport_fac[sport].items()):
            if count >= sport_lim[sport]:
                team = count // sport_lim[sport]
                spare = count % sport_lim[sport]
                output.append(f'{fac}({team},{spare})')
    output.append('\n')

print(''.join(output), end='')
