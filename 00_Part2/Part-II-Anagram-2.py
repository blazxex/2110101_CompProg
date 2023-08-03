import string
def anagram(t1,t2,dict_1,dict_2):
    remove_list = []
    for x in dict_1:
        if x not in dict_2:
            remove_list.append([x,dict_1[x]])
        elif dict_1[x]> dict_2[x]:
            remove_num = dict_1[x]-dict_2[x]
            remove_list.append([x,remove_num])
    remove_list.sort()
    return remove_list

def out_text(text,to_remove):
    print(text)
    if len(to_remove)==0:
        print('- None')
    for i in range(1,len(to_remove)+1):
        if to_remove[i-1][1]>1:
            print(' -','remove',to_remove[i-1][1],to_remove[i-1][0]+"'s")
        else:
            print(' -','remove',to_remove[i-1][1],to_remove[i-1][0])


text_1 = input().strip()
text_2 = input().strip()
text_1_dict ={}
text_2_dict = {}
new = ''


for x in text_1:
    x = x.lower()
    if x not in string.punctuation and x!= ' ':
        if x in text_1_dict:
            text_1_dict[x]+=1
        else:
            text_1_dict[x] = 1
for x in text_2:
    x = x.lower()
    if x not in string.punctuation and x!= ' ':
        if x in text_2_dict:
            text_2_dict[x]+=1
        else:
            text_2_dict[x] = 1
out_text(text_1,anagram(text_1,text_2,text_1_dict,text_2_dict))
out_text(text_2,anagram(text_2,text_1,text_2_dict,text_1_dict))



