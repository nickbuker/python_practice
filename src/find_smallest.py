def smallest(n):
    int_lst = map(int, list(str(n)))
    int_srt = sorted(int_lst)
    for i in xrange(len(int_lst)):
        if int_lst[i] == int_srt[i]:
            continue
        else:
            j = int_lst.index(int_srt[i])
            int_lst.insert(i, int_lst.pop(j))
            new_num = int("".join(map(str, int_lst)))
            return [new_num, j, i]
