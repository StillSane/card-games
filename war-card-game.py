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

  def deal(self, player_one, player_two):
    count = 0
    while self.deck:
      if self.deck:
        player_one.cards.append(self.deck.pop(0))
      if self.deck:
        player_two.cards.append(self.deck.pop(0))

  def __repr__(self):
    list = []
    for card in self.deck:
      list.append(card.name)
    return str(list)
  
class Player:
  def __init__(self, name):
    self.name = name
    self.cards = []
    self.score = 0

  def update_score(self):
    for card in self.cards:
      self.score += card.value
  
  def __repr__(self):
    self.update_score()
    return "{name} has {cards} cards and a score of {score}.".format(name=self.name, cards=len(self.cards), score=self.score)

class Game():
  def __init__(self, player_name):
    self.playing_area = {}
    self.player_one = Player(player_name)
    self.player_two = Player("The Computer")
    self.deck = Deck()
    self.winner = ""
    print(self.deck)
    self.deck.deal(self.player_one, self.player_two)

  def start(self):
    ready = input("Are you ready to play? (YES to begin/NO to end game)").upper()
    if ready == "YES":
      self.play_game()
    if ready == "NO":
      self.end_game()

  def play_game(self):
    pass

  def end_game(self):
    self.player_one.update_score()
    self.player_two.update_score()
    if self.player_one.score > self.player_two.score:
      print("{player_one_name} has beaten {player_two_name} with a score of {player_one_score} and {player_one_cards} cards. {player_two_name} had a score of {player_two_score} and {player_two_cards} cards.".format(player_one_name=self.player_one.name, player_two_name=self.player_two.name, player_one_score=self.player_one.score, player_two_score=self.player_two.score, player_one_cards=len(self.player_one.cards), player_two_cards=len(self.player_two.cards)))
    elif self.player_two.score > self.player_one.score:
      print("{player_two_name} has beaten {player_one_name} with a score of {player_two_score} and {player_two_cards} cards. {player_one_name} had a score of {player_one_score} and {player_one_cards} cards.".format(player_one_name=self.player_one.name, player_two_name=self.player_two.name, player_one_score=self.player_one.score, player_two_score=self.player_two.score, player_one_cards=len(self.player_one.cards), player_two_cards=len(self.player_two.cards)))
    else:
      print("It's a tie! {player_one_name} had a score of {score} and {player_one_cards} cards at the end of the game. {player_two_name} had a score of {score} and {player_two_cards} cards.".format(player_one_name=self.player_one.name, player_two_name=self.player_two.name, score=self.player_one.score, player_one_cards=len(self.player_one.cards), player_two_cards=len(self.player_two.cards)))

player_name = input("What is your name?")
new_game = Game(player_name)
new_game.start()
