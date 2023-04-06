# def add_poly(p1, p2):
#     op = []
#     new_p1 = p1.copy()
#     new_p2 = p2.copy()
#     for (a,b) in p1:
#         for (c,d) in p2:
#             if b == d:
#                 op.append((a+c,b))
#                 new_p1.remove((a,b))
#                 new_p2.remove((c,d))
#     op = op+new_p1+new_p2
#     op = sorted(op , key=lambda x:x[1],reverse=True)
#     op = [(x,y) for (x,y) in op if x!= 0]
#     return op
                
# def mult_poly(p1, p2):
#     mult= []
#     new_mult = []
#     for (a,b) in p1:
#         for (c,d) in p2:
#             mult.append((a*c,b+d))
#     mult = sorted(mult , key=lambda x:x[1],reverse=True)
#     for i in range(0,len(mult)-1):
#         if mult[i][1] == mult[i+1][1]:
#             new_mult.append((mult[i][0]+mult[i+1][0],mult[i][1]))
            
#         else:
#             new_mult.append((mult[i][0],mult[i][1]))
#             if len(mult)-2 ==i:
#                 new_mult.append((mult[i+1][0],mult[i+1][1]))
         
#     return mult
def add_terms(t1, t2):
    return (t1[0] * t2[0], t1[1] + t2[1])

def add_poly(p1, p2):
    result = []
    for term1 in p1:
        for term2 in p2:
            result.append(add_terms(term1, term2))
    return result

def combine_terms(poly):
    combined = {}
    for coeff, exp in poly:
        if exp in combined:
            combined[exp] += coeff
        else:
            combined[exp] = coeff
    return [(coeff, exp) for exp, coeff in sorted(combined.items(), key=lambda x: x[0], reverse=True)]

def mult_poly(p1, p2):
    multiplied = add_poly(p1, p2)
    return combine_terms(multiplied)

p1 = [(1,10),(2,8),(2,7),(2,5),(2,4),(5,3)]
p2 = [(2,6),(3,5),(2,4),(3,3),(5,1),(-9,0)]
print(mult_poly(p1, p2))