n,m,k = [int(a) for a in input().split()]
grad_fac = {}
guest_fac = {}
for i in range(n):
    grad,fac = input().split()
    grad_fac[grad] = fac
for j in range(m):
    inp = input().split()
    guest = inp[0]
    grad = inp[1:]
    for std in grad:
        if guest not in guest_fac:
            guest_fac[guest] = set([grad_fac[std]])
        else:
            guest_fac[guest] =  guest_fac[guest] | set([grad_fac[std]])
for l in range(k):
    txt = input().split()
    same = guest_fac[txt[0]]
    for name in txt:
        same&=guest_fac[name]
    if len(same) == 0:
        print('None')
    else:
        print(' '.join(sorted(list(same))))
# 8 3 2
# Luffy faculty_a
# Nami faculty_a
# Sanji faculty_b
# Zoro faculty_c
# Robin faculty_c
# Chopper faculty_a
# Brook faculty_c
# Franky faculty_b
# Eren Nami Chopper Brook
# Anya Sanji Luffy
# Yaiba Franky
# Eren Anya
# Anya Eren Yaiba


# 8 2 1
# Luffy faculty_a
# Nami faculty_a
# Sanji faculty_b
# Zoro fac_c
# Robin fac_c
# Chopper faculty_a
# Brook fac_c
# Franky faculty_b
# Shinji Sanji Chopper
# Amuro Zoro Sanji Nami
# Amuro Shinji