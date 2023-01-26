def str2hms(hms_str):
 t = hms_str.split(':')
 return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
 return ('0'+str(h))[-2:] + ':' + \
 ('0'+str(m))[-2:] + ':' + \
 ('0'+str(s))[-2:]

def to_sec(h,m,s):
 return ((h*3600) + (m*60) + s)

def to_hms(s):
  hour = (s//3600)
  mins = ((s%3600)//60)
  sec = (s%60)
  return hour, mins , sec

def diff(h1,m1,s1,h2,m2,s2):
    k = to_sec(h2,m2,s2) - to_sec(h1,m1,s1)
    return to_hms(k)

def main():
 hms_start = input()
 hms_end = input()
 h1,m1,s1 = str2hms(hms_start)
 h2,m2,s2 = str2hms(hms_end)
 dh,dm,ds = diff(h1,m1,s1,h2,m2,s2)
 print (hms2str(dh,dm,ds))
exec(input()) # DON'T remove this line