delivery = {'E':1,'Q':3,'N':7,'F':14}
month = [31,28,31,30,31,30,31,31,30,31,30,31]

def date_calcurator(d,m,y,add):
    month_check = month.copy() 
    add_date = d+add
    if y%400==0 or (y%4==0 and y%100!= 0):
        month_check[1]+=1
    if add_date<=month_check[m-1]:
        return 'd'+'/'+'m'+'/'+'y'
    else:
        d = month_check[m-1]-add_date
        m +=1
        if m==13:
            m=1
            y+=1
    return 'd'+'/'+'m'+'/'+'y'
        
            
def invalid_date(order):
    month_check = month.copy() 
    y= int(order[2])
    m = int(order[1])
    d = int(order[0])
    if y%400==0 or (y%4==0 and y%100!= 0):
        month_check[1]+=1
    if 0<d<=month_check[m-1]:
        return False
    else: return True
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

def calculate_delivery(delivery):
    num,delivery_type,d,m,y = delivery.split()
    print(date_calcurator(int(d),int(m),int(y),delivery[delivery_type]))

# command = input().split()
Error =[]
delivery_time =[]
# while True:
#     if command==['END']:
#         break
#     validate =check_Invalid(command)
#     if validate!=False:
#         Error.append(['Error:',command,'-->',validate])
#     if validate==True:
#         delivery_time.append(calculate_delivery(command))
#     command = input().split()
# print(Error)
        
print(calculate_delivery('10008 F 28 12 2560'))