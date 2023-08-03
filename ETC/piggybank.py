class piggybank:
    def __init__(self):
        self.one = 0
        self.two = 0
        self.five = 0
        self.ten = 0
    def add1(self,n):
        self.one+=n
    def add2(self,n):
        self.two+=n
    def add5(self,n):
        self.five+=n
    def add10(self,n):
        self.ten+=n
    def __int__(self):
        return self.one + (self.two*2)+ (self.five*5)+ (self.ten*10)
    def __lt__(self,rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return '{1:'+str(self.one)+', 2:'+str(self.two)+', 5:'+str(self.five)+', 10:'+str(self.ten)+'}'
    
cmd1 = 'p1.add1(1);p1.add2(3);p1.add5(2);p1.add10(3)'.split(';')
cmd2 = 'print(int(p1),str(p1))'.split(';')
p1 = piggybank(); p2 = piggybank() 
if '{1:1, 2:3, 5:2, 10:3}' == str(p1):
    print('r')
else:
    print('s')
for c in cmd1: eval(c)
for c in cmd2: eval(c)