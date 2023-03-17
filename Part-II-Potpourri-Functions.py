def convex_polygon_area(p):
    det = p+p[:1]
    plus,minus = 0,0
    for i,x in enumerate(det[:-1]):
        for a,b in det[i+1:i+2]:
            plus += x[0]*b
            minus += a*x[1]
            
    return float(abs(plus-minus)*0.5)
    
def is_heterogram(s):
    text = {}
    for x in s.lower():
        if 'a'<=x<='z':
            if x not in text :
                text[x]=1
            else: 
                return False
    return True
def replace_ignorecase(s,a,b):
    i = 0
    len_replace = len(a)
    new_str = ''
    while i < len(s):
        if str(s[i:i+len_replace]).lower() == a.lower():
           # print(str(s[i:i+len_replace]).lower(),a.lower())
            new_str += b
            i+=len_replace-1
        else: 
            new_str+= s[i]
            # i = len(new_str)
        i+=1
        
    return new_str
            
            
       
    
def top3(votes):
    vote_list = sorted([[-1*votes[x],x] for x in votes])
    return [name for vote,name in vote_list[:3]]
    

for k in range(2):
    exec(input().strip())

