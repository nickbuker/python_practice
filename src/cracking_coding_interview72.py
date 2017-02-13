class CallCenter(object):

    def __init__(self):
        self.dir = [1]
        self.man = [1,1,1]
        self.resp = [1,1,1,1,1,1]

    def dispatch_call(self):
        if any(self.resp):
            return self.allocate(self.resp)
        if any(self.man):
            return self.allocate(self.man)
        if any self.dir:
            return self.allocate(self.dir)
        return 'Busy'

    def allocate(self, emp):
        for i in range(emp):
            if emp[i]:
                emp[i] = 0
                return i

    def hang_up(self, emp, i):
        emp[i] = 1
