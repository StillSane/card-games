import random

class Card:
  types_to_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13}
  suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
  def __init__(self, type, suit):
    self.name = "{type} of {suit}".format(type = type, suit = suit)
    self.type = type
    self.suit = suit
    self.value = Card.types_to_values[type]

  def __repr__(self):
    return "This card, the {name}, is worth {value} points.".format(name=self.name, value=self.value)
  
class Deck:
  def __init__(self):
    self.deck = []
    for type in Card.types_to_values.keys():
      for suit in Card.suits:
        self.deck.append(Card(type, suit))
    self.length = len(self.deck)
    self.shuffle()

  def shuffle(self):
    random.shuffle(self.deck)

  def __repr__(self):
    list = []
    for card in self.deck:
      list.append(card.name)
    return str(list)
  
print(Deck())