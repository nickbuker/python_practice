def evil(n):
    bins = find_bin(n)
    if sum(bins) % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"

def find_bin(n):
    bins = []
    while n >= 1:
        rem = n % 2
        n =  n // 2
        bins.append(rem)
    return bins
