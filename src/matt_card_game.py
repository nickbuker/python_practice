'''
The deck contains 4 diamonds, 4 starts and 52 other cards. You have a card game
where you are dealt 5 cards, if you have a diamond in your hand, you can
discard it for 3 new cards. What is the probability of ending the game with a
star in your hand?.
'''

import random
import numpy as np


def trials(n=1000):
    results = []
    for i in range(n):
        results.append(game())
    return np.mean(results)


def game():
    deck = make_deck()
    hand, deck = deal_hand(deck)
    hand = discard(hand)
    hand, deck = draw_cards(hand, deck)
    return check_star(hand)


def make_deck():
    deck = 52 * ['other']
    deck.extend(4 * ['star'])
    deck.extend(4 * ['diamond'])
    random.shuffle(deck)
    return deck


def deal_hand(deck):
    hand = []
    for n in range(5):
        hand.append(deck.pop(-1 - n))
    return hand, deck


def discard(hand):
    return [card for card in hand if card != 'diamond']


def draw_cards(hand, deck):
    for n in range(3 * (5 - len(hand))):
        hand.append(deck.pop(-1 - n))
    return hand, deck


def check_star(hand):
    return 'star' in hand
