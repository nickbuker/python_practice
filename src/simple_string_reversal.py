"""
In this Kata, we are going to reverse a string while maintaining spaces.

For example:
solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"

https://www.codewars.com/kata/simple-string-reversal/train/python
"""


def solve(s):
    if s.find(' ') == -1:
        return s[::-1]
    spaces = []
    for i, c in enumerate(s):
        if c == ' ':
            spaces.append(i)
    s = s.replace(' ', '')[::-1]
    for space in spaces:
        s = s[:space] + ' ' + s[space:]
    return s
