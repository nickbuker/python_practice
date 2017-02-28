import time
from copy import copy

class Sorter(object):

    def __init__(self, arr):
        self.arr = arr
        self.comp, self.edits = 0, 0

    def sort(self, sort_type='bubble'):
        time0 = time.time()
        if sort_type == 'bubble':
            sorted_arr = self._bubble(self.arr)
        elif sort_type == 'quick':
            sorted_arr = self._quicksort(self.arr)
        else:
            print 'Not valid sort technique.'
        print '\ncomparisons: {} \nedits: {}'.format(self.comp, self.edits)
        print 'time: {}s\n'.format(time.time() - time0)
        return sorted_arr

    def _bubble(self, arr):
        new_arr = copy(arr)
        active = True
        self.comp, self.edits = 0, 0
        while active:
            active = False
            for i in xrange(1, len(new_arr)):
                x = new_arr[i - 1]
                y = new_arr[i]
                self.comp += 1
                if x > y:
                    new_arr[i], new_arr[i - 1] = x, y
                    active = True
                    self.edits += 1
        return new_arr

    def _quicksort(self, arr):
        new_arr = copy(arr)
        if len(new_arr) > 1:
            left, equal, right = [], [], []
            pivot = new_arr[-1]
            for n in new_arr:
                self.comp += 1
                if n < pivot:
                    self.edits += 1
                    left.append(n)
                self.comp += 1
                if n == pivot:
                    self.edits += 1
                    equal.append(n)
                self.comp += 1
                if n > pivot:
                    self.edits += 1
                    right.append(n)
            return self._quicksort(left) + equal + self._quicksort(right)
        else:
            return new_arr

    def _merge_sort(self, arr):
        pass
