def RLE(t):
    out = []
    t = t+' '
    count=1
    for i in range(len(t)-1):
        if t[i]==t[i+1]:
            count+=1
        else:
            out.append([t[i],count])
            count=1
    return out

exec(input())
    