import time
from copy import copy


class Sorter(object):
    def __init__(self, arr):
        self.arr = arr

    def sort(self, sort_type='quick'):
        time0 = time.time()
        new_arr = self._copy_and_counts(self.arr)
        if sort_type == 'bubble':
            sorted_arr = self._bubble(new_arr)
        elif sort_type == 'quick':
            sorted_arr = self._quicksort(new_arr)
        elif sort_type == 'merge':
            sorted_arr = self._merge_sort(new_arr)
        else:
            print 'Not a valid sort technique.'
        print '\ncomparisons: {} \nedits: {}'.format(self.comp, self.edits)
        print 'time: {}s\n'.format(time.time() - time0)
        return sorted_arr

    def _copy_and_counts(self, arr):
        self.comp, self.edits = 0, 0
        new_arr = copy(arr)
        return new_arr

    def _compare(self, n1, n2):
        self.comp += 1
        if n1 > n2:
            self.edits += 1
            return True
        return False

    def _bubble(self, arr):
        active = True
        while active:
            active = False
            for i in xrange(1, len(arr)):
                x = arr[i - 1]
                y = arr[i]
                if self._compare(x, y):
                    arr[i], arr[i - 1] = x, y
                    active = True
                    self.edits += 1
        return arr

    def _quicksort(self, arr):
        if len(arr) > 1:
            left, equal, right = [], [], []
            pivot = arr[-1]
            for n in arr:
                if self._compare(pivot, n):
                    left.append(n)
                elif self._compare(n, pivot):
                    right.append(n)
                else:
                    self.edits += 1
                    equal.append(n)
            return self._quicksort(left) + equal + self._quicksort(right)
        else:
            return arr

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
                self.comp += 2
                if self._compare(sorted_right[j], sorted_left[i]):
                    new_arr.append(sorted_left[i])
                    i += 1
                else:
                    new_arr.append(sorted_right[j])
                    j += 1
                    self.edits += 1
            if self._compare(len(sorted_left), i):
                new_arr += sorted_left[i:]
            if self._compare(len(sorted_right), j):
                new_arr += sorted_right[j:]
            return new_arr
        return arr
