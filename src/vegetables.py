def count_vegetables(string):
    veg_dict = {}
    for veg in string.split():
        if veg not in "cabbagecarrotcelerycucumbermushroomonionpepperpotatotofuturnip":
            continue
        if veg in veg_dict:
            veg_dict[veg] += 1
        else:
            veg_dict[veg] = 1
    return sorted([(v,k) for k,v in veg_dict.iteritems()], reverse=True)
