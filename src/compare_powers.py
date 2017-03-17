def compare_powers(n1, n2):
    if n1[0] == n2[0]:
        return cmp(n2[1], n1[1])
    if n1[1] == n2[1]:
        return cmp(n2[0], n1[0])
    return cmp(n2[0] ** n2[1], n1[0] ** n1[1])
