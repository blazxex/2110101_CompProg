# define the size of the square spiral (must be odd)
n = 7

# check that n is odd
if n % 2 == 0:
    print("Error: n must be odd.")
    exit()

# initialize the spiral with zeros
spiral = [[0 for i in range(n)] for j in range(n)]

# define the starting position at the center of the matrix
x, y = n//2, n//2

# define the initial direction
dx, dy = 0, 1

# fill the spiral with continuous integers starting with 1
for i in range(1, n*n+1):
    spiral[x][y] = i
    # check if the next position is out of bounds or already filled
    if (x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n or spiral[x+dx][y+dy] != 0):
        dx, dy = dy, -dx  # rotate direction
    x, y = x+dx, y+dy

# print the spiral
for i in range(n):
    for j in range(n):
        print("{:2d}".format(spiral[i][j]), end=" ")
    print()
