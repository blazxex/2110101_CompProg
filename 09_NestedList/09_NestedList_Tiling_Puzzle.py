def row_number(t, e): # return row number of t containing e (top row is row #0)
    count = 0
    for i,x in enumerate(t):
        for y in x:
            if y ==e:
                return i 
def flatten(t): 
    new = []
    for r in t:
        new+=r
    if 0 in new:
        new.remove(0)
    return new
def inversions(x):
    count = 0
    new_list = x.copy()
    for i in range(len(new_list)):
        for j in range(i,len(new_list)):
            if new_list[i]> new_list[j]:
                count+=1
    return count
        
    
def solvable(t):
    row = len(t)
    zero = row_number(t,0)
    inversion_n = inversions(flatten(t))
    if row%2 == 1 and inversion_n%2 ==0:
        return True
    elif row%2 == 0:
        if inversion_n %2 == 1 and zero%2 ==0:
            return True
        if inversion_n %2 == 0 and zero %2 == 1:
            return True
            
    return False


print(row_number([[0,8,7],[6,5,4],[3,2,1]], 0))