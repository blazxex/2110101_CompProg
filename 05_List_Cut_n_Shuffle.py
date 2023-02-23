def cut(card):
    half = int(len(card)/2)
    card = card[half:]+card[:half]
    return card

def spread(card):
    half = int(len(card)/2)
    new_card=[]
    a = card[:half]
    b = card[half:]
    for i in range(len(a)):
        new_card.append(a[i])
        new_card.append(b[i])
    return new_card

in_card = input().split()
order = input()
for x in order:
    if x =='S':
        in_card = spread(in_card)
    if x=='C':
        in_card = cut(in_card)
print(' '.join(in_card))
        