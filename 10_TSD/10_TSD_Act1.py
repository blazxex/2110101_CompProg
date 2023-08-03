name_sport = {}
for i in range(int(input())):
    name,sport = input().split()
    sport = sport.split(',')
    name = name.strip()
    sport = [x.strip() for x in sport]
    name_sport[name] = sport
 
while True:
    text = input().split()
    if text == ['q']:
        break
    sport_1 = set(name_sport[text[0]])
    sport_2 = set(name_sport[text[1]])
    print(sorted(list(sport_1&sport_2)))

