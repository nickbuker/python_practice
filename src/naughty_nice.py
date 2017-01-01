def whatListAmIOn(actions):
    karma = 0
    for action in actions:
        if action[0] in "bfk":
            karma += -1
        if action[0] in "gsn":
            karma += 1
    if karma > 0:
        return "nice"
    else:
        return "naughty"
