def is_odd(n):
    if n%2 ==1:
        return True
    return False

def has_odds(x):
    for num in x:
        if is_odd(num):
            return True
    return False

def all_odds(x):
    for num in x :
        if not is_odd(num):
            return False
    return True

def no_odds(x):
    if has_odds(x):
        return False
    return True

def get_odds(x):
    lst = []
    for num in x:
        if is_odd(num):
            lst.append(num)
    return lst

def zip_odds(a,b):
    new_lst = []
    one = get_odds(a)
    two = get_odds(b)
    str_len = max(len(one),len(two))
    for i in range(str_len):
        if i < min(len(one),len(two)):
            new_lst.append(one[i])
            new_lst.append(two[i])
        else:
            try:
                new_lst.append(one[i])
            except:
                new_lst.append(two[i])
    return new_lst

exec(input().strip())