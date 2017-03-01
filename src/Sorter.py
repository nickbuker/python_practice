import time
from copy import copy

class Sorter(object):

    def __init__(self, arr):
        self.arr = arr

    def sort(self, sort_type='bubble'):
        time0 = time.time()
        if sort_type == 'bubble':
            self.comp, self.edits = 0, 0
            sorted_arr = self._bubble(self.arr)
        elif sort_type == 'quick':
            self.comp, self.edits = 0, 0
            sorted_arr = self._quicksort(self.arr)
        elif sort_type == 'merge':
            self.comp, self.edits = 0, 0
            sorted_arr = self._merge_sort(self.arr)
        else:
            print 'Not valid sort technique.'
        print '\ncomparisons: {} \nedits: {}'.format(self.comp, self.edits)
        print 'time: {}s\n'.format(time.time() - time0)
        return sorted_arr

    def _bubble(self, arr):
        new_arr = copy(arr)
        active = True
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
        if len(arr) > 1:
            split = len(arr) // 2
            left, right = arr[:split], arr[split:]
            self.edits += 2
            sorted_left = self._merge_sort(left)
            sorted_right = self._merge_sort(right)
            new_arr = []
            i, j = 0, 0
            while i < len(sorted_left) and j < len(sorted_right):
                self.comp += 1
                if sorted_left[i] < sorted_right[j]:
                    new_arr.append(sorted_left[i])
                    i += 1
                    self.edits += 1
                else:
                    new_arr.append(sorted_right[j])
                    j += 1
                    self.edits +=1
            self.comp += 1
            if i < len(sorted_left):
                new_arr += sorted_left[i:]
                self.edits += 1
            self.comp += 1
            if j < len(sorted_right):
                new_arr += sorted_right[j:]
                self.edits += 1
            return new_arr
        return arr
