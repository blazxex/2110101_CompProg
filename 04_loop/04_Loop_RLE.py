text = input()
text = text+' '
count=1
for i in range(len(text)-1):
    if text[i]==text[i+1]:
        count+=1
    else:
        print(text[i],count,end=' ')
        count=1
    