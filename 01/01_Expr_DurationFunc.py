import math
def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
            ('0'+str(m))[-2:] + ':' + \
            ('0'+str(s))[-2:]
def to_sec(h,m,s):
    return (h*60*60)+(m*60)+s
def to_hms(s):
    h = math.floor((s/60)/60)
    m = math.floor((s-(h*60*60))/60)
    s = s%60
    return h,m,s
def diff(h1,m1,s1,h2,m2,s2):
    x = to_sec(h1,m1,s1)
    y = to_sec(h2,m2,s2)
    diffTime = y-x
    return to_hms(diffTime)


def main():
    hms_start = input()
    hms_end = input()
    h1,m1,s1 = str2hms(hms_start)
    h2,m2,s2 = str2hms(hms_end)
    dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
    print(hms2str(dh,dm,ds))



exec(input())
