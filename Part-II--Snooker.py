point = { 'R' : 1 ,
 'Y' : 2 ,
 'G' : 3 ,
 'W' : 4 ,
 'B' : 5 ,
 'P' : 6 ,
 'K' : 7 ,
 'X':0}
player_score = {'1':0, '2':0}
r = 7
colored = 6

def has_red(order):
    score = 0
    for ball in order:
        score += point[ball]
    return score

while True:
    turn = input()
    player = turn[0]
    order = turn[1:]
    player_score[player]+=has_red(order)
    if turn[1] =='K':
        break
    
score_1 = player_score['1']
score_2 = player_score['2']
print(score_1,score_2)
if score_1 == score_2:
    print('Tie')    
elif score_1> score_2:
    print('Player 1 wins')
else:
    print('Player 2 wins')

    
    
