# HW01 (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

def center(r):
  x= r[0]
  y = r[1]
  w =r[2]
  h= r[3]
  x_c = x+w/2
  y_c = y-h/2
  center_axis = []
  center_axis.append(x_c)
  center_axis.append(y_c)
  return center_axis
#======================================
def distance(r1, r2):
  axis_1=center(r1)
  axis_2=center(r2)
  dis = ((axis_1[0]-axis_2[0])**2+(axis_1[1]-axis_2[1])**2)**(1/2)
  return dis
#======================================
def intersection(r1, r2):
    ho_1 = [r1[0],r1[0]+r1[2]]
    ve_1 = [r1[1],r1[1]-r1[3]] 
    ho_2 = [r2[0],r2[0]+r2[2]]
    ve_2 = [r2[1],r2[1]-r2[3]]
    w= -max(ve_1[1],ve_2[1])+min(ve_1[0],ve_2[0])
    h= min(ho_1[1],ho_2[1])-max(ho_1[0],ho_2[0])
    
    return(max(0.0,w*h))

#======================================
def union(r1, r2):
   
    area1  =r1[2]*r1[3]
    area2 = r2[2]*r2[3]
    return area1+area2-intersection(r1,r2)
    







#======================================
def iou(r1, r2):
    return intersection(r1,r2)/union(r1,r2)







#======================================

r1=[1.0, 4.0, 1.5, 2.0]
r2=[2.0, 5.0, 2.5, 2.0]
r3=[4.0, 5.5, 1.5, 3.5]
r4=[6.0, 4.5, 1.5, 2.0]
r5=[5.75, 7.0, 2.0, 5.0]
r6=[-5.75, 7.0, 2.0, 5.0]
# print(center(r1))
# print(center(r2))
# print(round(distance(r1,r2),2))
# print(round(distance(r3,r4),2))

# print(intersection(r1,r2)) 
# print(intersection(r2,r3))
# print(intersection(r4,r5))
# print(intersection(r1,r5)) # กรณีโบนัส
# print(union(r1,r2))
# print(union(r2,r3))
# print(union(r4,r5))
# print(round(iou(r1,r2),2))
# print(round(iou(r2,r3),2))
# print(round(iou(r4,r5),2))
print(intersection(r4,r6))

# [1.75, 3.0]
# [3.25, 4.0]
# 1.8
# 2.02
# 0.5
# 1.0
# 3.0
# 0.0 # กรณีโบนัส
# 7.5
# 9.25
# 10.0
# 0.07
# 0.11
# 0.3