def match(word, pattern, include_chars, exclude_chars):
    include_list = [x for x in include_chars]
    if len(word)!= len(pattern):
        return False
    for i in range(len(word)):
        if word[i]!=pattern[i] and pattern[i]!= '?':
            return False
        if pattern[i]=='?':
            if word[i] in exclude_chars:
                return False
            if word[i] in include_list:
                include_list.remove(word[i])
                
   
    if len(include_list)!= 0:
        return False
        
   
    return True

print(match("MACMA", "M?C??", "AM", ""))
print(match("MACMA", "M?C??", "", "") )
print(match("MACMA", "M?C??", "", "CPE")) 
print(match("MACMA", "?????", "AAMM", "OK")) 
print(match("MACMA", "MACMA", "", "MACMA") )
print(match("MACMA", "M?C??", "AAA", "") )
print(match("MACMA", "M?C??", "MAX", "") )
print(match("MACMA", "M?C??", "C", "") )
print(match("MACMA", "M?C??", "", "MX") )
print(match("MACMA", "M?C???", "", "") )
print(match("MACMA", "M?C?", "", ""))