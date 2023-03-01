text = input().strip()
#print(ord('A'),ord('z'))
while text!= 'end':
    for a in text:
        if 'a'<=a.lower()<='m':
            print(chr(ord(a)+13),end='')
        elif 'n'<=a.lower()<='z':
            print(chr(ord(a)-13),end='')
        else:
            print(a,end='')
    text = input().strip()
    print()