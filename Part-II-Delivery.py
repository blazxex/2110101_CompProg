delivery = {'E':1,'Q':3,'N':7,'F':14}
month = [31,28,31,30,31,30,31,31,30,31,30,31]
Q = [] #[[y/m/date],order_num]
def date_calculator(d, m, y, add):
    d = int(d)
    m = int(m)
    y = int(y)
    month_check = [31,28,31,30,31,30,31,31,30,31,30,31] # List of days in each month
    add_date = d + add
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        month_check[1] += 1
    if add_date <= month_check[m - 1]:
        return str(add_date) + '/' + str(m) + '/' + str(y)
    else:
        add_date -= month_check[m - 1]
        m += 1
        if m == 13:
            m = 1
            y += 1
        return str(add_date) + '/' + str(m) + '/' + str(y)
          
def invalid_date(order):
    month_check = [31,28,31,30,31,30,31,31,30,31,30,31] # List of days in each month
    y = int(order[2])
    m = int(order[1])
    d = int(order[0])
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        month_check[1] += 1
    if 0 < d <= month_check[m-1]:
        return False
    else: 
        return True

def check_Invalid(order):
   
    date = order[2:]
    if int(date[2]) < 2558:
        return 'Invalid year'
    elif not (1<= int(date[1])<=12):
        return 'Invalid month'
    elif invalid_date(date):
        return 'Invalid date'
    elif order[1] not in delivery:
        return 'Invalid delivery type'
    return False

while True:
    queue = input()
    if queue=='END':
        break
    queue = queue.split()
    cmd =queue[1]
    
    if check_Invalid(queue)!= False:
        print('Error:',' '.join(queue),'-->',check_Invalid(queue))
    else:
        date = queue[2]        
        month_str = queue[3]
        year = queue[4]
        id = queue[0]
        Q.append([date_calculator(date,month_str,year,delivery[cmd]),id])
print(sorted(Q))

# 10002 E 29 -200 2550
# 10003 X 30 -200 2559
# 10001 Q 31 4 2558 
# 10004 N 29 5 2560 
# 10005 Q 10 4 2559 
# 10006 F 29 2 2560 
# 10007 X 28 2 2560
# 10008 F 28 12 2560
# 10009 E 1 1 2559
# 10010 N 29 5 2560
# END
