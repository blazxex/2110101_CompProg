grade_in = input().split()
sum =0.0
for x in grade_in:
    if x == 'A':
        sum+= 4.00
    elif x == 'B':
        sum+=3.00
    elif x == 'C':
        sum+= 2.00
    elif x == 'D':
        sum+= 1.00

print(round(sum/len(grade_in),2))