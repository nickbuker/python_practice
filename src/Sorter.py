import time

class Sorter(object):

    def __init__(self, arr):
        self.arr = arr

    def sort(self, sort_type='bubble'):
        time0 = time.time()
        if sort_type == 'bubble':
            comp, edits = self._bubble(self.arr)
        else:
            print 'Not valid sort technique.'
        print '\ncomparisons: {} \nedits: {}'.format(comp, edits)
        print 'time: {}s\n'.format(time.time() - time0)
        return self.arr

    def _bubble(self, arr):
        active = True
        comp, edits = 0, 0
        while active:
            active = False
            for i in xrange(1, len(arr)):
                x = arr[i - 1]
                y = arr[i]
                comp += 1
                if x > y:
                    arr[i], arr[i - 1] = x, y
                    active = True
                    edits += 1
        return comp, edits

    def _quicksort(self, arr):
        pass

    def _merge_sort(self, arr):
        pass
    
