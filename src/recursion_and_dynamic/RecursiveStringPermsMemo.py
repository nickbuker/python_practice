class PermsMemo(object):

    def __init__(self):
        self.memo = {}

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
                    if str(remains) in self.memo:
                        r_perms = self.memo[str(remains)]
                    else:
                        r_perms = self.perms(remains)
                        self.memo[str(remains)] = r_perms
                    for c in r_perms:
                        perm_list.append([a] + c)
        # remove duplicates
        results = []
        for perm in perm_list:
            if perm not in results:
                results.append(perm)
        # reset memo for future trials
        self.memo = {}

        return results
