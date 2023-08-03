
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
a = input().split(',')
b = input().split(',')
a_split = a[0].split()
b_split = b[0].split()
a_name = a_split[0]
b_name = b_split[0]
a_month = month.index(a_split[1])  
b_month = month.index(b_split[1]) 
a_date = int(a_split[2]) 
b_date = int(b_split[2]) 
a_year = int(a[1])
b_year = int(b[1])
a_tran=[a_year,a_month,a_date]
b_tran=[b_year,b_month,b_date]
if a_tran>b_tran:
    print(b_name)
elif a_tran<b_tran:
    print(a_name)
else:
    print(a_name,b_name)
