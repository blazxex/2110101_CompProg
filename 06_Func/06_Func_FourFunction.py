def make_int_list(x):
    return [int(y) for y in x.split()]
def is_odd(e):
    if e %2==1:
        return True
    return False
# คืนค่ําจริงเมื่อ e เป็นจํานวนคี่ ถ้ําไม่ใช่ คืนค่ําเท็จ
def odd_list(alist):
    alis=[]
    for num in alist:
        if is_odd(num):
            alis.append(num)
    return alis
            
            
# คืนlist ที่มีค่ําเหมือนalist แต่มีเฉพําะตวั ที่เป็นจํานวนคี่
# เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
def sum_square(alist):
    sum=0
    for z in alist:
        sum+=z**2
    return sum

# คืนผลรวมของกําลังสองของแต่ละค่ําในalist
# เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไปgrader
