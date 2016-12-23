from collections import Counter,defaultdict
from operator import mul

def numeric_palindrome(*args):
    n_list = map(int, list(str(reduce(mul, args))))
    return max(find_pals(n_list))

def find_pals(n_list):
    counts = Counter(n_list)
    tup = zip(counts.values(), counts.keys())
    c_dict = reduce(lambda x, (k,v): x[k].append(v) or x, tup, defaultdict(list))
    return pals

def construct_pal(c_dict):
    lefts, rights = [], []
    m = max(c_dict)
    if m % 2 == 0:







    # for n in xrange(0, len(n_list)):
    #     for m in xrange(n, len(n_list) + 1):
    #         if n < m:
    #             frag = n_list[n:m]
    #             if len(frag) == 1:
    #                 pals.append(int(frag[0]))
    #             if frag == frag[::-1] and len(frag) > 1:
    #                 pals.append(int(''.join(map(str, n_list[n:m]))))
