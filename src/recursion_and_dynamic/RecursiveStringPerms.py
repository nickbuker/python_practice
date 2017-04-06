class Perms(object):

    def __init__(self):
        pass

    def perms(self, s):
        perm_list = []
        if len(s) <= 1:
            return [s]
        # get pivot char
        for i, a in enumerate(s):
            perm_list.append([a])
            # get perms of remaining chars
            remains = []
            for j, b in enumerate(s):
                if i != j:
                    remains.append(b)
                    r_perms = self.perms(remains)
                    for c in r_perms:
                        perm_list.append([a] + c)
        # remove duplicates
        results = []
        for perm in perm_list:
            if perm not in results:
                results.append(perm)

        return results
