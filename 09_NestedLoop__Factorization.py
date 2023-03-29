def factor(N):
    i = 2
    count = 0
    num = []
    while i<=N:
        if N % i ==0:
            count +=1
            N = N / i
        else:
            if count!=0:
                num.append([i,count])
            count = 0
            i+=1
    num.append([i,count])
    return num
exec(input().strip()) 