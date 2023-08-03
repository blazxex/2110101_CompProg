numpad = {
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz',
    '0':' '   
}
new = {'abc': '2', 'def': '3', 'ghi': '4', 'jkl': '5', 'mno': '6', 'pqrs': '7', 'tuv': '8', 'wxyz': '9', ' ': '0'}

def text2keys( text ):
    a=''
    for alp in text.lower():
        if 'a'<='alp'<='z' or alp==' ':
            for key in new.keys():
                if alp in key:
                    a+= new[key] * (key.index(alp)+1)+' '
    return a
            
            
def keys2text( keys ):
    a= ''
    num = keys.split()
    for x in num:
        a+= numpad[x[0]][len(x)-1]
    return a

# exec(input().strip())

print(text2keys("I am busy"))