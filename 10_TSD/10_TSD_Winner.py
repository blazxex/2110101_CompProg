win = []
lose = []
for i in range(int(input())):
    mat = input().split()
    win.append(mat[0])
    lose.append(mat[1])
win = set(win)
lose = set(lose)
itc = win.intersection(lose)
never_lose = sorted(list(win-itc))
print(never_lose)
    
    