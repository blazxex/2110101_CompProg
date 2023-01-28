code=['01','02','20','21','22','23','23','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','51','53','55','58']
x = input()
check=0
for i in range(len(code)):
    if x == code[i]:
        check =1
if check == 1:
    print('OK')
else:
    print('Error')