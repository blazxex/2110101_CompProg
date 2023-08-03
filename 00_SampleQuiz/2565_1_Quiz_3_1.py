team_country = {}
country_team = {}
for i in range(int(input())):
    team,country = input().split()
    team_country[team] = country
while True:
    set_country = set()
    list_country = []
    status = True
    order = input().strip()
    if order == 'q':
        break
    order = order.split()
    for ft in order:
        if ft not in team_country:
            print('Not OK')
            status = False
            break
        else:
            set_country = set_country | set([team_country[ft]])
            list_country.append(team_country[ft])
    if status:
        if len(set_country) != len(list_country):
            print('Not OK')
        else:
            print('OK')



# 10
# Liverpool England
# ManCity England
# Bayern Germany
# Dortmund Germany
# Barcelona Spain
# Milan Italy
# PSG France
# Ajax Holland
# Real Spain
# Celtic Scotland
# Liverpool Dortmund Milan Ajax 
# Liverpool Barcelona PSG Real 
# ManCity Milan PSG Ajax Celtic 
# ManCity Ajax SamyanFC Real Bayern
# q