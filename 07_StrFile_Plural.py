text = input().strip()
es = ['s','x','ch']
vowel = ['a','e','i','o','u']


if text[-1] in es  or text[-2:] in es:
    print(text+'es')
elif text[-1] =='y' and text[-2] not in vowel:
    print(text[:-1]+'ies')
else:
    print(text+'s')
