def bucket_of(said):
    water = False
    slime = False
    said = said.lower()
    for w in ["wet","water","wash"]:
        if w in said:
            water = True
    for s in ["i don't know","slime"]:
        if s in said:
            slime = True
    if water == slime == True:
        return "sludge"
    if water == True:
        return "water"
    if slime == True:
        return "slime"
    return "air"
