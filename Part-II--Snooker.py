point = { 'R ' : 1 ,
 'Y ' : 2 ,
 'G ' : 3 ,
 'W ' : 4 ,
 'B ' : 5 ,
 'P ' : 6 ,
 'K ' : 7  }
player_score = {'1':0, '2':0}


def not_falue(frame,red):
    if red!=0:
        if frame[0]!='R':
            return False
    else:
        red-=1
        return True
        
    
def check_score(turn,red):
    player = turn[0]
    play = turn[1:]
    if not_falue(play,red):
        for x in range(len(play)):
            player_score[player]+=point[x]
        
        
        
    
red = 7
turn = 0
while turn!='2X':
    turn = input().strip()
    check_score(turn,red)
print(player_score)
    
    