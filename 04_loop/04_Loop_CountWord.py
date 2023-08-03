word = input()
sentence = input()
sign = ['"','(',')',',','.','\'']
count = 0
for i in range(len(sign)):
    sentence = sentence.split(sign[i])
    sentence = ' '.join(sentence)
sentence = sentence.split()

for j in range(len(sentence)):
    if word == sentence[j]:
        count+=1
print(count)
