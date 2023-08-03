x = [int(e) for e in input().split()]
num = int(input())
back = x[:len(x)-num]
front = x[-num:]
print(front+back)
