def reverse(dna):
    new_dna = ''
    for x in dna:
        if x == 'A':
            new_dna += 'T'
        elif x=='T':
            new_dna += 'A'
        elif x=='G':
            new_dna += 'C'
        elif x=='C':
            new_dna += 'G'
    return new_dna[::-1]

def fequence(dna,cliq):

    feq = [0]*4
    for x in dna:
        if x in cliq:
            feq[cliq.index(x)]+=1
    a = 'A='+str(feq[0])
    t = 'T='+str(feq[1])
    g = 'G='+str(feq[2])
    c = 'C='+str(feq[3])
    x = [a,t,g,c]
    return ', '.join(x)

def duplicate(dna,dup):
    count = 0
    for i in range(len(dna)-1):
        if dna[i:i+2] ==dup:
            count+=1
    return count

def check_dna(dna,cliq):
    for x in dna:
        if x not in cliq:
            return False
    return True    
            
    
cliq = ['A','T','G','C']
dna = input().strip().upper()
oper = input().strip()
if check_dna(dna,cliq):
    if oper =='R':
        print(reverse(dna))
    elif oper =='F':
        print(fequence(dna,cliq))
    elif oper == 'D':
        dup = input().strip()
        print(duplicate(dna,dup))
else:
    print('Invalid DNA')
    
    
