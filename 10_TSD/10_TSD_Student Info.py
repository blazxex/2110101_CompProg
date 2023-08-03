info = []
for i in range(int(input())):
    info.append(input().split())
info.sort()
cmd = set(input().split())
x = 0
for std in info:
    if cmd<=set(std[1:]):
        x+=1
        print(' '.join(std))
if x == 0:
    print('Not Found')

# 8
# Krit A 97 CP
# Oat A 98 CE
# Pim C 99 CP
# Pun C 97 CHE
# Jame Dog 100 CE
# Art C 97 CP
# Benz Dog 99 CP
# Mark C 100 CP
# CP C

# 8
# Krit A 97 CP
# Oat A 98 CE
# Pim C 99 CP
# Pun C 97 CHE
# Jame Dog 100 CE
# Art C 97 CP
# Benz Dog 99 CP
# Mark C 100 CP
# CE