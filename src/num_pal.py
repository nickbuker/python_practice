from collections import Counter, defaultdict
from operator import mul


def numeric_palindrome(*args):
    n_list = map(int, list(str(reduce(mul, args))))
    return max(find_pals(n_list))


def find_pals(n_list):
    counts = Counter(n_list)
    tup = zip(counts.values(), counts.keys())
    c_dict = reduce(lambda x, (k, v): x[k].append(v) or x, tup, defaultdict(list))
    return pals


def construct_pal(c_dict):
    lefts, rights = [], []
    m = max(c_dict)
    if m % 2 == 0:
        pass
