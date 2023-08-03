score = input().split()
scoreInt = [float(x) for x in score]
max=0
min= scoreInt[0]
for i in range(len(score)):
    if min > scoreInt[i]:
        min = scoreInt[i]
    if max < scoreInt[i]:
        max = scoreInt[i]

print(round((sum(scoreInt)-max-min)/2,2))
