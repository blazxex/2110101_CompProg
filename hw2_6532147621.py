# HW02_Selection_Loop (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

#-----------------------------
# Riemann sum functions
#-----------------------------
def riemann_left(f, a, b, n):
    x = (b-a)/n
    arg = a
    s_left = 0
    for i in range(n):
        s_left += (f(arg))
        arg += x 
    y=s_left*x
    return y

def riemann_right(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Right rule
    x =(b-a)/n
    arg = a+x
    s_right = 0
    for j in range(n):
        s_right += f(arg)
        arg+= x
    
    return s_right*x

def riemann_mid(f, a, b, n):
    # คืนค่าเป็นจำนวนจริงของ Riemann sum โดยใช้ Midpoint rule
    x =(b-a)/n
    arg = a+(x/2)
    s_mid = 0
    for k in range(n):
        s_mid += f(arg)  
        arg+= x
    return s_mid*x

def riemann_trap(f, a, b, n):
    x =(b-a)/n
    arg = a+x
    s_trap = 0
    front = f(a)
    back = f(b)

    for l in range(n-1):
      s_trap += 2*f(a)
      a+=x
    return (s_trap+front+back)*x*0.5

#-----------------------------
def estimate(riemann_sum_function, f, a, b, precision):
    k=1
    while True:
        if round(riemann_sum_function(f,a,b,k),precision)==round(riemann_sum_function(f,a,b,k+1),precision):
            break
        else: k+=1
    riemann_sum = riemann_sum_function(f,a,b,k)

    return [round(riemann_sum, precision), k] # ห้ามลบหรือแก้ไขบรรทัดนี้

