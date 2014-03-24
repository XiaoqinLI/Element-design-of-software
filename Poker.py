## File: Poker.py
## Description: Five card draw, which is very interesting.
##              In game, there are 2~6 people. In each game, there is either a winner or some ties
##              Total time consumed: 3 hours
## Author: Xiaoqin LI
## Date Created: 02/01/2014
## Date Last Modified:02/04/2014

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
  SUITS = ('C', 'D', 'H', 'S')

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
    if self.rank == 14:
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
  
  # operation overriding
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

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)    # a list of object cards: a card deck
        
  # shuffle card deck
  def shuffle (self):
    random.shuffle (self.deck)
    
  # draw a card on top of deck
  def deal (self):
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)
      
class Poker (object):
  def __init__ (self, numHands):
    self.deck = Deck()
    self.deck.shuffle()
    self.hands = []

    # each hand draw 5 cards from deck.
    numCards_in_Hand = 5
    for i in range (numHands):
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  def play (self):
    score_hands = []
    rank_hands = []
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True)  # get the current hand of cards and sort it in descending order.
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)

      #Judge the rank of current hand and assign points to this hand based on the rank
      current_score = self.is_royal(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Royal')
        continue
      
      current_score = self.is_straight_flush(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Straigt Flush')
        continue
      
      current_score = self.is_four(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Four of Kind')
        continue
      
      current_score = self.is_full(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Full House')
        continue

      current_score = self.is_flush(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Flush')
        continue

      current_score = self.is_straight(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Straight')
        continue

      current_score = self.is_three(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Three of a Kind')
        continue

      current_score = self.is_two(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'Two Pair')
        continue

      current_score = self.is_one(sortedHand)
      if current_score != 0:
        score_hands.append(current_score)
        rank_hands.append('Hand ' + str(i+1)+': '+'One Pair')
        continue
      else:
        score_hands.append(self.is_high(sortedHand))
        rank_hands.append('Hand ' + str(i+1)+': '+'High Card')
        continue

    # print rank of each hand in game
    print()
    for i in range(len(self.hands)):
      print(rank_hands[i])
    print()

    # determin the winner of the game.
    max_score = max(score_hands)
    max_index_list = []

    # determin how many and which hands have the max point
    # determin if there are ties or winner in game.
    # If there are ties then print out the hands in ascending order
    # If not then print out a winner.
    for i in range(len(score_hands)):
      if score_hands[i] == max_score:
        max_index_list.append(i+1)
 
    if len(max_index_list) != 1: 
      for i in range(len(max_index_list)):
        print('Hand ' + str(max_index_list[i]) + ' ties.')
    else:
      print('Hand ' + str(max_index_list[0]) + ' wins.')

  # determine if current hand is royal    
  def is_royal (self, currenthand):
    h_score = 10
    if currenthand[0].rank == 14:
      for i in range(len(currenthand)-1):
        if currenthand[i].rank - currenthand[i+1].rank != 1 or currenthand[i].suit != currenthand[i+1].suit:
          return 0     
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    else:
      return 0
    
  # determine if current hand is straight flush      
  def is_straight_flush (self, currenthand):
    h_score = 9
    for i in range(len(currenthand)-1):
      if currenthand[i].rank - currenthand[i+1].rank != 1 or currenthand[i].suit != currenthand[i+1].suit:
        return 0     
    score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
            currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
    return score

  # determine if current hand is four of a kind      
  def is_four (self, currenthand):
    h_score = 8
    if currenthand[0].rank == currenthand[3].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    if currenthand[1].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[4].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[0].rank
      return score
    else:
      return 0

  # determine if current hand is full of house      
  def is_full (self, currenthand):
    h_score = 7
    if currenthand[0].rank == currenthand[2].rank and currenthand[3].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    if currenthand[0].rank == currenthand[1].rank and currenthand[2].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[2].rank*13**4 + currenthand[3].rank*13**3 + \
              currenthand[4].rank*13**2 + currenthand[1].rank*13 + currenthand[0].rank
      return score
    else:
      return 0
    
  # determine if current hand is flush
  def is_flush (self, currenthand):
    h_score = 6
    for i in range(len(currenthand)-1):
      if currenthand[i].suit != currenthand[i+1].suit:
        return 0
    score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
            currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
    return score

  # determine if current hand is straight
  def is_straight (self, currenthand):
     h_score = 5
     for i in range(len(currenthand)-1):
       if currenthand[i].rank - currenthand[i+1].rank != 1:
         return 0     
     score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
             currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
     return score

  # determine if current hand is three of a kind 
  def is_three (self, currenthand):
    h_score = 4
    if currenthand[0].rank == currenthand[2].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    elif currenthand[1].rank == currenthand[3].rank:
      score = h_score*13**5 + currenthand[1].rank*13**4 + currenthand[2].rank*13**3 + \
              currenthand[3].rank*13**2 + currenthand[0].rank*13 + currenthand[4].rank
      return score
    elif currenthand[2].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[2].rank*13**4 + currenthand[3].rank*13**3 + \
              currenthand[4].rank*13**2 + currenthand[0].rank*13 + currenthand[1].rank
      return score
    else:
      return 0
    
  # determine if current hand is two pair 
  def is_two (self, currenthand):
    h_score = 3
    if currenthand[0].rank == currenthand[1].rank and currenthand[2].rank == currenthand[3].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    elif currenthand[0].rank == currenthand[1].rank and currenthand[3].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[3].rank*13**2 + currenthand[4].rank*13 + currenthand[2].rank
      return score
    elif currenthand[1].rank == currenthand[2].rank and currenthand[3].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[1].rank*13**4 + currenthand[2].rank*13**3 + \
              currenthand[3].rank*13**2 + currenthand[4].rank*13 + currenthand[0].rank
      return score
    else:
      return 0
    
  # determine if current hand is one pair 
  def is_one (self, currenthand):
    h_score = 2
    if currenthand[0].rank == currenthand[1].rank:
      score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
              currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    elif currenthand[1].rank == currenthand[2].rank:
      score = h_score*13**5 + currenthand[1].rank*13**4 + currenthand[2].rank*13**3 + \
              currenthand[0].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
      return score
    elif currenthand[2].rank == currenthand[3].rank:
      score = h_score*13**5 + currenthand[2].rank*13**4 + currenthand[3].rank*13**3 + \
              currenthand[0].rank*13**2 + currenthand[1].rank*13 + currenthand[4].rank
      return score
    elif currenthand[3].rank == currenthand[4].rank:
      score = h_score*13**5 + currenthand[3].rank*13**4 + currenthand[4].rank*13**3 + \
              currenthand[0].rank*13**2 + currenthand[1].rank*13 + currenthand[2].rank
      return score
    else:
      return 0

  # assign points to a high card hand 
  def is_high (self, currenthand):
    h_score = 1
    score = h_score*13**5 + currenthand[0].rank*13**4 + currenthand[1].rank*13**3 + \
            currenthand[2].rank*13**2 + currenthand[3].rank*13 + currenthand[4].rank
    return score
  
# start the game
def main():
  numHands = int (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))
  print()
  game = Poker (numHands)
  game.play()
main()
