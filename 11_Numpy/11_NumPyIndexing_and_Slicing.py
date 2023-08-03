import numpy as np
def f1(v):
# v: 1-D numpy array
    n = np.arange(len(v))
    return np.array_equal(n,v)

def f2(u, v):
# # u and v are 1-D numpy array of equal size
    # n = u.shape[0]
    # y = v.T
    # return n+y
    n = u.shape[0]
    x = v[::-1]
    return u+x
def f3(M, v):
# M: 2-D numpy array
# v: 1-D numpy array
# note: v.shape[0] equals to M.shape[1] 
    A = []
    print(M)
    print(v)    
    for i in range(M.shape[0]):
        a = []
        for j in range(M.shape[1]):
            a.append(M[i,j] * v[j]) 
        A.append(a)
    return np.array(A), v*M
    # return M*v
print(f3(np.array([[1,2],[3,4]]),np.array([1,2])))
    
    



exec("import dis\ndef has_loop(f):\n b = dis.Bytecode(f)\n for e in b:\n  ar = e.argrepr\n  if '<listcomp>' in ar or '<setcomp>' in ar or '<dictcomp>' in ar or (e.opname=='JUMP_ABSOLUTE' and e.argval<e.offset):\n   return True\n return False")

u = np.array([2, 4, 8, 9]); v = np.array([7,3,1,2])
print(f2(u,v).tolist(), f2(u,v[::-1]).tolist())