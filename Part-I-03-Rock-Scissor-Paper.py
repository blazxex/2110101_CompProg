def check(a,b,count_a,count_b):
    
    if a == b:
        pass
    elif a=='R':
        if b =='P':
            count_b+=1
        elif b =="S":
            count_a +=1
    elif a=='P':
        if b =='S':
            count_b+=1
        elif b =="R":
            count_a +=1
    elif a=='S':
        if b =='R':
            count_b+=1
        elif b =="P":
            count_a +=1
    return count_a,count_b
        
count_a = 0
count_b=0

num = int(input())
for i in range(0,num*3):
    x,y = input().split()
    count_a,count_b = check(x,y,count_a,count_b)    
    if count_a == num:
        print(count_a,count_b)
        print('Player 1 wins')
        break
    elif count_b == num:
        print(count_a,count_b)
        print('Player 2 wins')
        break
    elif count_a==count_b and i==(num*3)-1:
        print(count_a,count_b)
        print('Tie')
        break
    elif count_a!=count_b and i==(num*3)-1:
        print(count_a,count_b)
        print('Tie')
        break
    
    