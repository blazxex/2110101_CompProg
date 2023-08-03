class piggybank:
    def __init__(self):
        self.coins = {}
    def sum_cn(self):
        lst = 0
        for (a,b) in self.coins.items():
            lst +=b
        return lst
    
    def add(self,v,n):
        if v not in self.coins:
            if self.sum_cn()+n<=100:
                self.coins[float(v)] = n
            else:
                return False
        else:
            if self.sum_cn()+n>100:
                return False
            else:
                self.coins[float(v)]+=n
        print(self.sum_cn())
        return True
    
    def __float__(self):
        total = 0.0
        for x in self.coins:
            total+=self.coins[x]*x
        return total
    def __str__(self):
        lst = [[c,amt] for (c,amt) in self.coins.items()]
        lst.sort()
        out = []
        for a,b in lst:
            out.append(str(a)+':'+str(b))
        return '{'+', '.join(out)+'}'

cmd1 = 'p1.add(5,90);print(p1.add(1,11));print(str(p1))'.split(';')
# cmd2 = 'print(p2.add(1,101));print(str(p2));print(p2.add(1,100));print(str(p2))'.split(';')
p1 = piggybank(); p2 = piggybank() 
for c in cmd1: eval(c)
# for c in cmd2: eval(c)        
        
        