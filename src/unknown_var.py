def the_var(vars):
    lets = 'abcdefghijklmnopqrstuvwxyz'
    return sum([lets.index(x) + 1 for x in vars.split("+")])
