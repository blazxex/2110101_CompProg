text_1 = [x.lower() for x in input().replace(" ",'')]
text_2 = [x.lower() for x in input().replace(" ",'')]
text_1.sort()
text_2.sort()
if text_1 == text_2:
    print('YES')
else:
    print('NO')
