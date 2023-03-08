import string #Found return Flase not found Retrun True
def no_lowercase(t):
    for x in t:
        if 'a'<=x<='z':
            return False
    return True
def no_uppercase(t): 
    for x in t:
        if 'A'<=x<='Z':
            return False
    return True
def no_number(t): 
    for x in t:
        if '0'<=x<='9':
            return False
    return True
def no_symbol(t):
    for x in t:
        if x in string.punctuation:
            return False
    return True
def character_repetition(t):
    for i in range(len(t)-3):
        if t[i]==t[i+1]==t[i+2]==t[i+3]:
            return True
    return False
    
def number_sequence(t):
    num = '01234567890'
    for i in range(len(t)-3):
        a = str(t[i:i+4])
        b = a[::-1] 
        if '0'<=t[i]<='9':
            if a in num or b in num:
                return True
    return False
            
def letter_sequence(t):
    for i in range(len(t)-3):
        if 'a'<= t[i].lower() <='z':
            a = t[i].lower()
            b = t[i+1].lower()
            c = t[i+2].lower()
            d = t[i+3].lower()
            if ord(a)==ord(b)-1==ord(c)-2==ord(d)-3:
                return True
            elif ord(a)==ord(b)+1==ord(c)+2==ord(d)+3:
                return True
    return False
def keyboard_pattern(t):
    l1 ='!@#$%^&*()-+'
    l2 ='qwertyuiop'
    l3='asdfghjkl'
    l4='zxcvbnm'
    
    for i in range(len(t)-3):
        a = str(t[i:i+4]).lower()
        b = a[::-1].lower()
        if (a in l1 or b in l1 or
            a in l2 or b in l2 or
            a in l3 or b in l3 or
            a in l4 or b in l4):
            return True 
    return False
    
passw = input().strip()


errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw): 
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
if len(errors) == 0:
    print('OK')
else:
    for x in errors:
        print(x)