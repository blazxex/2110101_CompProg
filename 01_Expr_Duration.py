h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1 * 60 * 60 + m1 * 60 + s1 #time is sec
t2 = h2 * 60 * 60 + m2 * 60 + s2
dt = t2 - t1 #diff in sec
dh =  dt // (60*60)#diff in hour ,floor division
hour = (24+dh)%24
dt -= dh * 60 * 60 # diff in sec - hour
dm = dt // 60 # diff in min
dt -= dm * 60
ds = dt
print(str(hour) + ":" + str(dm) + ":" + str(ds))
