import numpy as np
def sum_2_rows( M ):
    return M[::2]+M[1::2]

def sum_left_right(M):
    return M[:,::2] + M[:,2::2]

def sum_upper_lower(M):
    half = int(len(M)/2)
    upper = M[:half]
    lower = M[half:]
    return upper+lower
def sum_4_quadrants(M):
    (r,c) = M.shape
    hr = int(r/2)
    hc = int(c/2)
    fst= M[:hr,:hc] 
    snd= M[:hr,hc:] 
    trd= M[hr:,:hc] 
    fth=M[hr:,hc:] 
    return fst+snd+trd+fth

def sum_4_cells(M):
    return M[::2,::2]+ M[::2,1::2]+ M[1::2,::2]+ M[1::2,1::2]

def count_leap_years(years):
    years = years - 543 
    leap_years = years[(years % 4 == 0) & ((years % 100 != 0) | (years % 400 == 0))]
    return len(leap_years)

exec(input().strip())
