## File: Blackjack.py
## Description: Blackjack card game.
##              there are 2-6 players in each game, only the results from
##              players will be displayed.
##              Total time consumed: 2 hours
## Author: Xiaoqin LI
## Date Created: 02/04/2014
## Date Last Modified:02/10/2014

import string, math, random

class Card (object):
  RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
  SUITS = ('S', 'D', 'H', 'C')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if self.rank == 1:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit
  
  # operation overwriting
  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)
  
# create a list of object cards(Card): a card deck class
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)    
        
  # shuffle card deck
  def shuffle (self):
    random.shuffle (self.deck)
    
  def __len__ (self):
    return len (self.deck)

  # draw a card on top of deck
  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)

# create Player Class
class Player (object):
  def __init__ (self, cards): 
    self.cards = cards

  # add a card to a player
  def hit (self, card):
    self.cards.append(card)

  # get total points of a player at this moment
  def getPoints (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 1:
        count += 11
      else:
        count += card.rank

    # deduct 10 if Ace is there and needed as 1
    for card in self.cards:
      if count <= 21:
        break
      elif card.rank == 1:
        count = count - 10    
    return count

  # does the player have "Blackjack" or not
  def hasBlackjack (self):
    return (len (self.cards) == 2 and self.getPoints() == 21)

  # str overwriting to print a player's current hand and points
  def __str__ (self):
    hand = ''
    points = self.getPoints()
    for card in self.cards:
      hand = hand + str(card) + ' '
    points_string = '- ' + str(points) + ' points'     
    return hand + points_string
  
# Dealer class inheriting from the Player class
class Dealer (Player):
  def __init__ (self, cards):
    Player.__init__ (self, cards)
    self.show_one_card = True

  # over-load the hit function()
  # add cards while points < 17, then allow all to be shown
  def hit (self, deck):
    self.show_one_card = False
    while self.getPoints() < 17:
      self.cards.append (deck.deal())

  # return just one card if not hit yet, retrun all cards if start hitting
  def __str__ (self):
    if self.show_one_card:
      return str(self.cards[0])
    else:
      return Player.__str__(self)

# Blackjack game class
class Blackjack (object):
  def __init__ (self, numPlayers):
    self.deck = Deck()
    self.deck.shuffle()

    self.numPlayers = numPlayers
    self.players = []

    for i in range (self.numPlayers):
      self.players.append (Player([self.deck.deal(), self.deck.deal()]))

    self.dealer = Dealer ([self.deck.deal(), self.deck.deal()])

  def play (self):
    # Print the cards that each player has
    for i in range (self.numPlayers):
      print ('Player ' + str(i + 1) + ': ' + str(self.players[i]))

    # Print the cards that the dealer has
    print ('Dealer: ' + str(self.dealer))
    print()
    
    # Each player hits until he says no, no need to hit for a player who gets blackjack, 
    playerPoints = []
    for i in range (self.numPlayers):
      points = (self.players[i]).getPoints()
      if points == 21:
        playerPoints.append (points)
        continue
      else:
        while True:
          choice = input ('Player ' + str(i + 1) + ', do you want to hit? [y / n]: ')
          if choice in ['y', 'Y']:
            (self.players[i]).hit (self.deck.deal())
            points = (self.players[i]).getPoints()
            print ('Player ' + str(i + 1) + ': ' + str(self.players[i]))
            if points >= 21:
              break
          else:
            break 
      playerPoints.append (points)
      print()

    # After all players, dealer's turn to hit
    self.dealer.hit(self.deck)
    dealerPoints = self.dealer.getPoints()
    print ('Dealer: ' + str(self.dealer) + ' - ' + str(dealerPoints))
    print ()

    # Judge who win and who lose in all players
    if dealerPoints > 21:
      for i in range(self.numPlayers):
        if playerPoints[i] <= 21:
          print('Player ' + str(i+1) + ' wins')
        else:
          print('Player ' + str(i+1) + ' loses')        
    else:
      for i in range(self.numPlayers):
        if dealerPoints < playerPoints[i] <= 21:
          print('Player ' + str(i+1) + ' wins')
        elif dealerPoints <= 21 < playerPoints[i]:
          print('Player ' + str(i+1) + ' loses')
        elif dealerPoints == playerPoints[i]:
          if self.players[i].hasBlackjack() and not self.dealer.hasBlackjack():
            print('Player ' + str(i+1) + ' wins')
          elif not self.players[i].hasBlackjack() and self.dealer.hasBlackjack():
            print('Player ' + str(i+1) + ' loses')
          else:
            print('Player ' + str(i+1) + ' ties')
        else:
          print('Player ' + str(i+1) + ' loses')
          
# main function, start a game           
def main ():
  numPlayers = eval (input ('Enter number of players: '))
  while (numPlayers < 1 or numPlayers > 6):
    numPlayers = eval (input ('Enter number of players: '))
  game = Blackjack (numPlayers)
  game.play()

main()

