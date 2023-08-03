def knows(R,x,y):
    if y in R[x] :
        return True
    return False
def is_celeb(R,x):
    
    know = set(R[x]) - set([x])
    if know != set():
        return False
    for a,know_name in R.items():
        if x not in know_name and a!=x :
            return False
    return True

def find_celeb(R):
    for person in R:
        if is_celeb(R,person):
            return person
    return None

def read_relations():
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1:
            break
        if d[1] not in R:
            R[d[1]] = set()
        if d[0] not in R:
            R[d[0]] = {d[1]}
        else:
            R[d[0]] = R[d[0]] | {d[1]}
    return R


def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)

exec(input().strip())
