def convolute(M,K):
    return sum([sum([M[i][j]*K[i][j] for i in range(len(M))])  for j in range(len(M[0]))])
exec(input().strip())