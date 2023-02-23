result = input().strip()
target = int(input())
frame = 1
total_score = 0
score_in_frame= []

x=len(result)+5
i=0
while i<len(result)-1:
    if i==len(result)-3 and result[i]=='X':
        if result[i:i+3] =='XXX':
            score_in_frame.append(30)
            break
        elif result[i:i+2] =='XX':
            score_in_frame.append(20+int(result[i+2]))
            break
    if result[i] == 'X':
        if result[i:i+3] =='XXX':
            score_in_frame.append(30)
        elif result[i:i+2] == 'XX':
            score_in_frame.append(20+int(result[i+2]))
        elif result[i+2]=='/':
            score_in_frame.append(20)
        else: score_in_frame.append(10+int(result[i+1])+int(result[i+2]))
    elif result[i] == '/':
        if result[i+1]=='X':
            score_in_frame.append(20)
        else: score_in_frame.append(10+int(result[i+1]))
    elif result[i+1] != '/' :
        score_in_frame.append(int(result[i])+int(result[i+1]))
        i+=1
    i+=1
if 1<=target<=10:
    print(score_in_frame[target-1])
else: print(sum(score_in_frame))
print()
x = abs(
for i in range()