name = [x.strip() for x in input().split(',')]
name_2 = [a[0].upper()+a[1:].lower() for a in name]
print(' '.join(name_2))