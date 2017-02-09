def card_game(arr):
    plays = [(n, i) for i, n in enumerate(arr)]
    ind = 0
    while lenp(plays) > 1:
        ind, plays = elim(ind, plays)
    return plays[0][1]


def elim(i, plays):
    card = plays[i][0] + i
    if card > len(plays):
        card = card % len(plays)
    plays.pop(card)
    if card > len(plays):
        card = 0
    return card, plays
