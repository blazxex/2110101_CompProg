n = int(input())
for i in range(n):
    old_text = input()
    new_text = old_text.lstrip('.')
    print('.'*int((len(old_text)-len(new_text))/2)+new_text)