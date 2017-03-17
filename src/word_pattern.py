def word_pattern(pattern, string):
    mapping = dict(zip(str(pattern), string.split()))
    return " ".join([mapping[c] for c in pattern]) == string \
        and len(mapping) == len(set(mapping.values()))
