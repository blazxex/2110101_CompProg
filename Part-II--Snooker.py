point = { 'R' : 1 ,
 'Y' : 2 ,
 'G' : 3 ,
 'W' : 4 ,
 'B' : 5 ,
 'P' : 6 ,
 'K' : 7  }
player_score = {'1':0, '2':0}
score= 0 
def check_falue(play,red):
    if red!= 0 and play[0]!= 'R':
        return True
    return False
def cal_score(order,red):
    player_id = order[0]
    play = order[1:]
    if check_falue(play,red) !=True:
        for x in play:
            if x != 'X':
                player_score[player_id] += point[x]
    

order = input()
red = 7
while order[1]!='K':
    player_id = order[0]
    if order[1]=='R':
        red-=1
    cal_score(order,red)
    order = input()
    print(player_score['1'],player_score['2'],red)
    

p1_score = player_score['1']
p2_score = player_score['2']
print(p1_score,p2_score)
if p1_score == p2_score:
    print("Tie")
elif p1_score<p2_score:
    print('Player 2 wins')
elif p1_score > p2_score:
    print('Player 1 wins')
