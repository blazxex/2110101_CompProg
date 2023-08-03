# def zip(a,b):
    
#     out = []
#     id_m = max(len(a),len(b))
#     id_min = min(len(a),len(b))
#     for x in range(id_min):
#         out.append(a[x])
#         out.append(b[x])
#     if len(a) == id_m:
#         return out+a[id_min:id_m+1]
#     else:return out+b[id_min:id_m+1]

# print(zip([-1,-2,-3], [10,20,30,40]))

# def reverse_digits(t):
#     num_idex = []
#     num =''
#     temp = list(t)
#     for i,text in enumerate(temp):
#         if '0'<= text <= '9':
#             num+=text
#             num_idex.append(i)
#     for j in range(len(num_idex)):
#         temp[num_idex[j]] = num[j]
        
#     return ''.join(temp)
# print(reverse_digits('You are 16 going on 17. A3B53'))
# import numpy as np
# def nearest(D, x):
#     temp = D-x
#     id = np.argmin(temp)
#     return D[id]
# def z_score(x):
#     return (x - np.std(x))/np.mean(x)
    
# print(z_score(np.array([3.1, 2.2, 4.5, 9.0])))

# def is_magic( D ):
#     expect_sum = np.sum[D[0]]
    
    
#     return re

# x = np.array([[8,11,14,1],[13,2,7,12],[3,16,9,6],[10,5,4,15]])
# print(is_magic(x))
# import numpy as np
# def sum(a):
#     (row,col) = a.shape
#     row = row//2
#     col = col//2
#     stQ = np.sum(a[:row,col:])
#     rdQ = np.sum(a[row:,:col])
#     return stQ+rdQ
# def get_student_GPA(g,c):
#     return np.sum(g,axis=0)/len(g)
# g = np.array([[1,1,1,1,1],[4,0,0,0,4],[4,4,4,4,4]]) 
# c = np.array([3,3,3,4,1])
# g.T
# print(g)
# x = np.identity(5)
# print(x)
#a = np.array([[1,2,3,4],[9,2,18,3],[7,3,12,0]])
# b = np.array([1,2,3,4])
# print(b[[True,True,False,False]])
# print(a>3)

# print(a[a>3])

import numpy as np
dice_rolls = np.array([3, 1, 5, 2, 5, 1, 1, 5, 1, 4, 2, 1, 4, 5, 3, 4, 5, 2, 4, 2, 6, 6, 3, 6, 2, 3, 5, 6, 5])

row = len(dice_rolls[dice_rolls>2])
print(row)