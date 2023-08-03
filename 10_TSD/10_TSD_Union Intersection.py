n = int(input())
if n-1 <0:
  print(0)
  print(0)
else:  
    x = set(input().split())
    un = x.copy()
    itc = x.copy()
    for i in range(n-1):
      a = set(input().split())
      un= un.union(a)
      itc = itc.intersection(a)
    print(len(un))
    print(len(itc))