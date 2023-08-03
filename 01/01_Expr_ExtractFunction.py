import math
def mosteller(w, h):
    return (math.sqrt(w*h))/60
def du_bois(w, h):
    return 0.007184*math.pow(w,0.425)*math.pow(h,0.725)
def fujimoto(w, h):
    return 0.008883*math.pow(w,0.444)*math.pow(h,0.663)
def main():
    weight = float(input())
    height = float(input())
    print("Mosteller =", round(mosteller(weight, height), 5))
    print("Du Bois =", round(du_bois(weight, height), 5))
    print("Fujimoto =", round(fujimoto(weight, height), 5))

exec(input()) # DON'T remove this line
