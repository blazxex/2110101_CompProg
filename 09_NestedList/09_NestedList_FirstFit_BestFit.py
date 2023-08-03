def first_fit(L,e):
    x = []
    for i,gp in enumerate(L):
        if sum(gp)+e <=100:
            L[i].append(e)
    return L.append(e)

def best_fit(L,e):
    max_value = 0
    max_index = -1
    for i,gp in enumerate(L):
        if sum(gp)+e <=100:
            if sum(gp)+e > max_value:
                max_value = sum(gp)+e
                max_index = i
    return L[max_index].append(e)

def partition_FF(D):
    l = []
    for e in D:
        first_fit(l,e)
    return l
        
        
        
            
    
L=[[50],[90]];best_fit(L,10);print(L)