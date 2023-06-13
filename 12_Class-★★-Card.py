class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    def getScore(self):
        if self.value =='A':
            return 1
        if self.value in ['J','Q','K']:
            return 10
        return int(self.value)
    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    def value_sort(self):
        if self.value=='2':
            return 15
        if self.value=='A':
            return 14
        if self.value=='K':
            return 13
        if self.value=='Q':
            return 12
        if self.value=='J':
            return 11
        return self.getScore()
    def __lt__(self, rhs):
        if self.value != rhs.value:
            return self.value_sort() < rhs.value_sort()
        else:
            return self.suit < rhs.suit
            

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])