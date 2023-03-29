inp = input().strip()
character = {}
order = []
while inp!='q':
    name,animal = inp.split(',')
    
    animal = animal.strip()
    name = name.strip()
    if animal not in character:
        character[animal] = name
        order.append(animal)
    else:
        character[animal]+= ', '+name
    inp = input().strip()
for x in order:
    print(x+':',character[x])
    
    
# Ted, bear
# Pongo, dog
# Fozzie, bear
# Winnie-the-Pooh, bear
# Nana, dog
# Hello Kitty, cat
# Scooby Doo, dog
# Garfield, cat
# Yogi, bear
# Tom, cat 
# Sylvester, cat
# Pluto, dog
# Goofy, dog