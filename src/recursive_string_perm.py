def permutations(s):
    # only one permutation of single char string
    if len(s) <= 1:
        return [s]

    perms = []
    # get pivot char
    for i, c in enumerate(s):
        perms.append([c])
        # get remaining chars
        remains = []
        for j, x in enumerate(s):
            if i != j:
                remains.append(x)
                # get permutations of remaining chars
                z = permutations(remains)
                # concat permutations of remaining chars to pivot char
                for t in z:
                    perms.append([c] + t)
    # remove duplicates
    results = []
    for word in perms:
        if word not in results:
            results.append(word)

    return results
