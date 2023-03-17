text = input()
text=text.replace(',',' ').split()
new_name = []
for name in text:
    new_name.append(name[0].upper()+name[1:].lower())
print(' '.join(new_name))