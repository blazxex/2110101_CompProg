def reverse(d):
    lst = []
    for x in d:
        lst.append([d[x],x])
    return dict(lst)
    
def keys (d,v):
    key =[]
    for x in d:
        if d[x]==v:
            key.append(x)
    return key

exec(input().strip())