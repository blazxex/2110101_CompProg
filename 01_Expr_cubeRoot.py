import math
def sqrt_n_times(x, n):
    for i in range(n):
        x = math.sqrt(x)
    return x
def cube_root(y):
    a = sqrty_n_times(y,2)
    b = a*sqrt_n_times(a,2)
    c = b*sqrt_n_times(b,4)
    d = c*sqrt_n_times(c,8)
    e = d * sqrt_n_times(d, 16)
    f = e * sqrt_n_times(e, 32)
    return f

def main():
    q = float(input())
    print(cube_root(q))

exec(input()) # DON'T remove this line
