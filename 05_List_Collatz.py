n = int(input())
li = [str(n)]
while n!=1:
    if n%2==0:
        n= int(n/2)
    else:
        n = 3*n +1
    li.append(str(n))
print('->'.join(li[-15:]))