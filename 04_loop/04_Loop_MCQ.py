solution = input()
answer = input()
count=0
if len(answer)!=len(solution):
    print('Incomplete answer')
else:
    for i in range(len(solution)):
        if solution[i]==answer[i]:
            count+=1    
    print(count)
