def short_form(s):
    return s[0] + "".join([c for c in s[1:-1] if c not in "aeiouAEIOU"]) + s[-1]
