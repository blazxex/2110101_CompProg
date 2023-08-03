enemy = []
ally ={}
while True:
    ipt = input().split()
    if ipt[0] == 'End':
        break
    if ipt[0] =='Ally':
        countries = set(ipt[1:])
        for country in countries:
            if country not in ally:
                ally[country] = countries
            else:
                ally[country] = ally[country] | countries
    elif ipt[0] == 'Enemy':
        countries = set(ipt[1:])
        for country in countries:
            if country not in ally:
                ally[country] = set([country])
        
        enemy.append(countries)
    elif ipt[0] == 'Table':
        print(enemy)
        lst_cty = ipt[1:] + ipt[1:2]
        status = True
        for c1,c2 in enemy:
            for i in range(len(lst_cty)-1):
                if lst_cty[i] in ally[c1] and lst_cty[i+1] in ally[c2]:
                    status = False
                if lst_cty[i] in ally[c2] and lst_cty[i+1] in ally[c1]:
                    status = False
        if status:
            print('Okay')
        else:
            print('No')
            
        
        
                
# Ally America England Ukraine France
# Ally Russia China
# Enemy China America
# Enemy France Iran
# Enemy Iran Iraq
# Table America England Iceland France Iran Russia Iraq
# Table America England Russia
# Table America England Thailand Russia China Iran China Japan
# End 