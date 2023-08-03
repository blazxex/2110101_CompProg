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

def test_center():
    ans  = [center([1, 5, 2, 2])]
    ans += [center([1, 5, 2, 4])]
    ans += [center([1, 5, 4, 2])]
    ans += [center([-1, 1, 4, 2])]
    ans += [center([10.5, 20.2, 6.6, 7.8])]
    soln = [[2.0, 4.0], [2.0, 3.0], [3.0, 4.0], [1.0, 0.0], [13.8, 16.3]]
    print('test_center', (ans==soln))
    
def test_distance():
    r = [[1, 4, 2, 2], [1, 1, 2, 2], [4, 4, 2, 2], [4, 1, 2, 2]]
    ans  = [round(distance(r[0], r[0]),6)]
    ans += [round(distance(r[0], r[1]),6)]
    ans += [round(distance(r[0], r[2]),6)]
    ans += [round(distance(r[0], r[3]),6)]
    ans += [round(distance(r[1], r[2]),6)]
    soln = [0.0, 3.0, 3.0, 4.242641, 4.242641]
    print('test_distance', (ans==soln))

def test_intersection():
    r = [
        [0, 40, 30, 30],
        [10, 60, 20, 30],
        [20, 30, 20, 10],
        [20, 20, 20, 30],
        [5, 35, 20, 20],
    ]
    ans  = [intersection(r[0], r[0])]
    ans += [intersection(r[1], r[0])]
    ans += [intersection(r[0], r[1])]
    ans += [intersection(r[2], r[0])]
    ans += [intersection(r[0], r[2])]
    ans += [intersection(r[3], r[0])]
    ans += [intersection(r[0], r[3])]
    ans += [intersection(r[4], r[0])]
    ans += [intersection(r[0], r[4])]
    soln = [900.0, 200.0, 200.0, 100.0, 100.0, 100.0, 100.0, 400.0, 400.0]
    print('test_intersection', (ans==soln))

def test_intersection_bonus():
    r = [
        [0, 40, 30, 30],
        [30, 60, 10, 2],
        [30, 40, 10, 20],
        [20, 70, 5, 30],
        [40, 70, 5, 5],
        [-10, 70, 5, 5],
    ]
    ans  = [intersection(r[0], r[0])]
    ans += [intersection(r[1], r[0])]
    ans += [intersection(r[0], r[1])]
    ans += [intersection(r[2], r[0])]
    ans += [intersection(r[0], r[2])]
    ans += [intersection(r[3], r[0])]
    ans += [intersection(r[0], r[3])]
    ans += [intersection(r[4], r[0])]
    ans += [intersection(r[0], r[4])]
    ans += [intersection(r[5], r[0])]
    ans += [intersection(r[0], r[5])]
    soln = [900.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print('test_intesection_bonus', (ans==soln))

def test_union():
    r = [
        [0, 40, 30, 30],
        [10, 60, 20, 30],
        [20, 30, 20, 10],
        [20, 20, 20, 30],
        [5, 35, 20, 20],
    ]
    ans  = [union(r[0], r[0])]
    ans += [union(r[1], r[0])]
    ans += [union(r[0], r[1])]
    ans += [union(r[2], r[0])]
    ans += [union(r[0], r[2])]
    ans += [union(r[3], r[0])]
    ans += [union(r[0], r[3])]
    ans += [union(r[4], r[0])]
    ans += [union(r[0], r[4])]
    soln = [900.0, 1300.0, 1300.0, 1000.0, 1000.0, 1400.0, 1400.0, 900.0, 900.0]
    print('test_union', (ans==soln))

def test_iou():
    r = [
        [0, 40, 30, 30],
        [10, 60, 20, 30],
        [20, 30, 20, 10],
        [20, 20, 20, 30],
        [5, 35, 20, 20],
    ]
    ans  = [round(iou(r[0], r[0]),6)]
    ans += [round(iou(r[1], r[0]),6)]
    ans += [round(iou(r[0], r[1]),6)]
    ans += [round(iou(r[2], r[0]),6)]
    ans += [round(iou(r[0], r[2]),6)]
    ans += [round(iou(r[3], r[0]),6)]
    ans += [round(iou(r[0], r[3]),6)]
    ans += [round(iou(r[4], r[0]),6)]
    ans += [round(iou(r[0], r[4]),6)]

    soln = [
            1.0,
            0.153846,
            0.153846,
            0.1,
            0.1,
            0.071429,
            0.071429,
            0.444444,
            0.444444,
          ]
    print('test_iou', (ans==soln))

test_center()
test_distance()
test_intersection()
test_union()
test_iou()