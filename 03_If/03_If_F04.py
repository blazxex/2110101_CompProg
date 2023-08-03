def is_mobile_number(number):
    firstDG= number[0]+number[1]
    if len(number)==10 and (firstDG == '06' or firstDG =='08' or firstDG =='09'):
        return True
    else:
        return False

exec(input())
 