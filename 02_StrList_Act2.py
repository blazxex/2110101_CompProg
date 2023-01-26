x = [int(e) for e in input().split()]
num = int(input())
back = x[num:]
front = x[:num]
print(back+front)
