# file_name = input().strip()
file_name = 'data.txt'
fn = open(file_name,'r')
line = fn.readlines()
line = [x.strip() for x in line]
cmd = line[0] 
if cmd == 'T2M':
    pattern = line[1]
    morse = ''
    for text in line[2:]:
        for e in text : 
            j = pattern.find('[' + e + ']') 
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        print(morse.strip())
elif cmd == 'M2T':
    pattern = line[1]
    


else:
    print('Invalid code')