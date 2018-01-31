"""
Define to_alternating_case(char*) such that each lowercase letter becomes uppercase and each
uppercase letter becomes lowercase.

https://www.codewars.com/kata/alternating-case-%3C-equals-%3E-alternating-case/train/python
"""

def to_alternating_case(s):
    alt = ''
    for c in s:
        if c == c.lower():
            alt += c.upper()
        else:
            alt += c.lower()
    return alt