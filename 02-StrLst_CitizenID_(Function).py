def check_digit(id):
    x=0
    for i in range(12):
        x += int(id[i]) * (13 - i)
    lastDigit = ((11 - x % 11)) % 10
    return lastDigit
exec(input())