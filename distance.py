import math
def distance (x1,y1,x2,y2):
  range = math.sqrt((y2-y1)**2+(x2-x1)**2)
  return range

d=distance(1,1,4,5)
print(d)
