def numeric_palindrome(*args):
    n_list = map(int, list(str(find_n(args))))
    return max(find_pals(n_list))

def find_n(args):
    num = 1
    for arg in args:
        num *= arg
    return num

def find_pals(n_list):
    pals = []
    for n in xrange(0, len(n_list)):
        for m in xrange(n, len(n_list) + 1):
            if n < m:
                frag = n_list[n:m]
                if len(frag) == 1:
                    pals.append(int(frag[0]))
                if frag == frag[::-1] and len(frag) > 1:
                    pals.append(int(''.join(map(str, n_list[n:m]))))
    return pals
