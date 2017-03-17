from collections import Counter


class List(object):
    def count_spec_digits(self, ints, digs):
        counts = Counter("".join(map(str, ints)))
        return [(int(k), counts[k]) if k in counts else (int(k), 0)
                for k in map(str, digs)]
