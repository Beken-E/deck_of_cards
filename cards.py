from random import randint, shuffle

class Cards:
    def __init__(self):
        pass
    masti = ["Черви", "Бубны", "Трефы", "Пики"]
    karty = {1: "Туз", 2: "2" , 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "Валет", 12: "Дама", 13: "Король"}
    
class Deck(Cards):
    deck = []
    def __init__(self):
        
        for i in self.karty.values():
            self.deck.append(i + " " + self.masti[0])
            self.deck.append(i + " " + self.masti[1])
            self.deck.append(i + " " + self.masti[2])
            self.deck.append(i + " " + self.masti[3])     

    def deal(self):
        q = 51
        r = randint(0, q)
        q -= 1
        l = self.deck.pop(r)
        return l
    
    def mix(self):
        shuffle(self.deck)
        return self.deck


deck = Deck()
    
print(deck.deal())
print(deck.mix())





