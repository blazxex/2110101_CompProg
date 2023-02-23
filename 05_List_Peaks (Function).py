def peaks(num):
    peak = []
    for i in range(1,len(num)-1):
        if num[i-1]<num[i] and num[i]>num[i+1]:
            peak.append(i)
    return peak

exec(input())