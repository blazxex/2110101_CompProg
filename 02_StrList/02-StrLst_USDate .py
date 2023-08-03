date = input()
monthStr = ['January','February','March','April','May','June','July','August','September','October','November','December']
splt=date.split('/')
print(monthStr[int(splt[1])-1],splt[0]+',',splt[2])