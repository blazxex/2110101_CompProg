doc = {}

def freq_index(vue,search):
    count = 0
    for x in vue:
        if x == search:
            count +=1
    return count / len(vue)

def spec_index(vue):
    return 1/len(set(vue))
    
for i in range(int(input())):
    name = input()
    word = input().split()
    doc[name] = word
while True:
    search_index = []
    search = input()
    if search == '-1':
        break
    for y in doc:
        search_index.append([freq_index(doc[y],search)*spec_index(doc[y]),y])
    search_index.sort(reverse=True)
    if search_index[0][0] > 0:
        print(search_index[0][1])
    else:
        print('NOT FOUND')
    
    
    



