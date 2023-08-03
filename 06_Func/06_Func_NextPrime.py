def is_prime(n): #ทดสอบวา่nเป็นจานวนเฉพาะหรอืไม่ 
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
                if n%k == 0:
                    return False
    return True

def next_prime(N):
    i = N+1
    while True:
        if is_prime(i) == True:
            break
        i+=1
    return i

def next_twin_prime(N):
    x = next_prime(N)
    y= next_prime(x)
    lst = []
    while True:
        if abs(y-x) == 2:
            lst.append(x)
            lst.append(y)
            break
        z=x
        x = next_prime(y)
        y = next_prime(z)
    lst.sort()
    return (lst[0],lst[1])
