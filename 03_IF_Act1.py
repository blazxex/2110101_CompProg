def checkday(day):
    if day=='Sunday':
        print('Red')
    elif day=='Monday':
        print('Yellow')
    elif day=='Tuesday':
        print('Pink')
    elif day=='Wednesday':
        print('Green')
    elif day=='Thursday':
        print('Orange')
    elif day=='Friday':
        print('Blue')
    elif day=='Saturday':
        print('Purple')
    else:
        print('Invalid day')

for i in range (4):
    day = input()
    checkday(day)


