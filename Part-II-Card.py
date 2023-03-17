# value_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T' ,'J','Q', 'K']
# set_card = ['C','D','H','S']
# def add_sign(a):
#     if int(a)>0:
#         return '+'+a
#     return a
    
# def check_set(a,b):
#     if a==b:
#         return '0'
#     else:
#         return add_sign(str(set_card.index(a)-set_card.index(b)))

# def check_card(a,b):
#     v_1 = a[0]
#     v_2= b[0]
#     if a==b:
#         return '0'
#     elif v_1==v_2:
#         return check_set(a[1],b[1])
#     else:
#         return add_sign(str(value_card.index(v_1)-value_card.index(v_2)))

# card = input().strip()
# card_set = (len(card))-2
# result = ''
# for i in range(0,card_set,2):
#     result += check_card(card[i:i+2],card[i+2:i+4])
# print(result)

# x = input()
d = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'C':1,'D':2,'H':3,'S':4}
l = [1,2,3,4,-5]
# for i in range(len(x)//2-1):
#     if d[x[2*i]] == d[x[2*i+2]]: 
#         l.append(d[x[2*i+1]]-d[x[2*i+3]])
#     else: 
#         l.append(d[x[2*i]] - d[x[2*i+2]])
for i in l:
    if i>0: print('+%d' %i,end='')
    else: print(i,end='')
# print('+%d')