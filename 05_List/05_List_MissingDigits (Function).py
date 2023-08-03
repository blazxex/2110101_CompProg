
def missing_digits(text):
    num = [0]*10
    missing = []
    for tt in text:
        if '0'<= tt <='9':
            num[int(tt)]+=1
    i = 0
    for k in num:
        if k == 0:
            missing.append(i)
        i+=1
    return missing

exec(input())
    
        