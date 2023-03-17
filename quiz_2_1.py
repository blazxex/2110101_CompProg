def point_of_word(text):
    point = 0
    for x in text:
        if x in 'AEILNORSTU':
            point+=1
        elif x in 'DG':
            point +=2
        elif x in 'BCMP':
            point += 3
        elif x in 'FHVWY':
            point+=4
        elif x in 'K':
            point +=5
        elif x in'JX':
            point+=8
        elif x in 'QZ':
            point+=10
    return point

word_list = input().split()
score = []
for x in word_list:
    score.append([-1*point_of_word(x),x])
score.sort()
for y in score:
    print(y[1],-1*y[0])