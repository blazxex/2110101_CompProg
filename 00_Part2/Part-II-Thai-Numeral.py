th_num = {
    '0':"soon",
'1':'neung',
'2':'song',
'3':'sam',
'4':'si',
'5':'ha',
'6':'hok',
'7':'chet',
'8':'paet',
'9':'kao',
'10':'sip'
}

def to_Thai(N):
    str_n = str(N)
    out = ''
    if N>= 1000:
        out+=th_num[str_n[-4]] +' '+ 'pun '
    if N>= 100:
        if str_n[-3]!= '0':
            out+= th_num[str_n[-3]] +' '+ 'roi '
    if N>= 10:
        if '10'<=str(str_n[-2:])<='19':
            out+=  th_num['10']+' '
        elif str_n[-2]!= '0':
            if str_n[-2] == '2':
                out+= 'yi'+' '+ th_num['10']+' '
            else:
                out+= th_num[str_n[-2]]+' '+ th_num['10']+' '
    if str_n[-1]!= '0':
        if N>10 and str_n[-1]=='1':
            if str_n[-1]=='1':
                out+='et'
        else:
            out+= th_num[str_n[-1]]
    if N == 0:
        out = th_num['0']
    return out
for k in range(0,9): print(to_Thai(k))