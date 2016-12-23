import string

def find_missing_letter(chars):
    lows_dict, ups_dict = make_lists()
    if chars[0].islower():
        return check_dict(chars, lows_dict)
    if chars[0].isupper():
        return check_dict(chars, ups_dict)

def make_lists():
    lows, ups = string.lowercase, string.uppercase
    return make_dicts(lows), make_dicts(ups)

def make_dicts(lets):
    return {lets[x]: lets[x+1] for x in xrange(0,25)}

def check_dict(chars, let_dict):
    for i in xrange(0, len(chars) - 1):
        if let_dict[chars[i]] != chars[i+1]:
            return let_dict[chars[i]]
