def rps(p1, p2):
    tup = (p1[0],p2[0])
    if tup[0] == tup[1]:
        return "Draw!"
    p1w = [("p","r"), ("r","s"), ("s","p")]
    p2w = [("r","p"), ("s","r"), ("p","s")]
    if tup in p1w:
        return "Player 1 won!"
    if tup in p2w:
        return "Player 2 won!"
    else:
        return "Not a valid selection"
