##############################
# APS106 Winter 2022 - Lab 6 #
##############################

import random
from itertools import combinations

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            deck.append([suit,number])

    return deck

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

#############################
# PART 1 - Deal card
#############################

def deal_card(deck,hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.
    
    Note that this function returns nothing! It modifies the two lists that 
    are passed in as parameters in place.

    """
    # TODO your code here  
    hand.append(deck[0])
    deck.remove(deck[0])
#deal_card([['spades', 10], ['hearts', 2], ['clubs', 8]],[['diamonds', 3]])
#############################
# PART 2 - Score Hand
#############################

def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parameter
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the 
    number of the card.
    """
    
    # TODO your code here
    
    # Count pairs
    score = 0
    cards = [item[1] for item in hand]
    for i in range(len(cards)):
        for j in range(i+1,len(cards)):
            if(cards[i]==cards[j]):
                score+=2
    
    # Count same suit
    suits = [item[0] for item in hand] 
    counts = {} 
    
    for item in suits: 
        if item in counts: 
            counts[item] += 1 
        else: 
            counts[item] = 1 
    
    max_key = None 
    max_count = 0 
    
    for key in counts: 
        if counts[key] > max_count: 
            max_count = counts[key] 
            max_key = key 
    if max_count>=4:
        score+=max_count
    
    
    # Count Runs
    subsets = [[],[],[],[],[]]
    sortedCards=cards
    sortedCards.sort()
    
    for i in range(0,len(cards)):
        if sortedCards[0] == sortedCards[i]-1:
            subsets[i] = [sortedCards[0]]
        else:
            if sortedCards[1] == sortedCards[i]-1:
                subsets[i] = [sortedCards[1]] 
            else:
                if sortedCards[2] == sortedCards[i]-1:
                    subsets[i] = [sortedCards[2]]  
                else:
                    subsets[i] = [-1]
    #print(subsets)
    for i in range(0,len(cards)):
        for j in range(1,len(cards)):
            #print(sortedCards[j], subsets[i][-1])
            if subsets[i][-1]==(sortedCards[j]-1):
                subsets[i]=subsets[i]+[sortedCards[j]]

    for item in subsets:
        if len(item)>=3:
            score+=len(item)
            
    # Sums of 15
    subsets = [[]]
    for elem in cards:
        for i in range(len(subsets)):
            if(elem>=10):
                subsets.append(subsets[i] + [10])
            else:
                subsets.append(subsets[i] + [elem])
    for subset in subsets:
        if sum(subset) == 15:
            score += 2
    
    return score
    
#score_hand([['diamonds', 5], ['diamonds', 12], ['diamonds', 13], ['diamonds', 1],['hearts', 5]])
################################
# PART 3 - PLAY
################################

def play(shuffled_deck):
    """
    (list) -> [str, int, int]
    
    Function deals cards to players, computes player scores, and
    determines winner.
    
    Function retuns a three-element list where the first element is a string
    indicating the winner, the second element is an int specifying player\'s
    score, and the third element is an int specifying dealer\'s score.
    """
    player_hand = []
    dealer_hand = []
    
    # TODO complete the function
    for i in range(0,10,2):
        #print(i,i+1)
        #print(shuffled_deck[i])
        dealer_hand.append(shuffled_deck[i])
        player_hand.append(shuffled_deck[i+1])

    dealer_score=score_hand(dealer_hand)
    player_score=score_hand(player_hand)
    if(dealer_score>=player_score):
        return ["dealer wins", player_score, dealer_score]
    else:
        return ["player wins", player_score, dealer_score]
