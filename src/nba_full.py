def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return round(ppg * (48. / mpg), 1)
