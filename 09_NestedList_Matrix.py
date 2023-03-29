def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m
def mult_c(c, A):
    for y in range(len(A)):
        for x in range(len(A[y])):
            A[y][x] *=c
    return A
def mult(A, B):
    
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0]) 
    
    sum = [[0 for row in range((cols_B))] for col in range(rows_A)]
    for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    sum[i][j] += float(A[i][k] * B[k][j])
    return sum

exec(input().strip())