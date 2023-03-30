


def in_all(malls):
    i = 0
    sum_mall = set()
    for x in malls.values():
        if i==0:
            sum_mall = set(x)
        else:
            sum_mall = x&sum_mall
        i+=1
    return sorted(list(sum_mall))

def only_one(malls):
    value_sum = []
    sum_v = set()
    for x in malls.values():
        value_sum.append(x)
        sum_v = sum_v | x
    for i in range(1,len(value_sum)):
        itc = value_sum[i-1] & value_sum[i]
        sum_v = sum_v - itc
    if len(sum_v) == 1:
        sum_v = sum_v - value_sum[0]-value_sum[len(value_sum)-1]
    return sorted(sum_v)
        
        
        
        
        
        


b = {'A':{'W'},'B':{'X'},'C':{'Y','Z'}};print(in_all(b));print(only_one(b))