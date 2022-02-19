heap_parent = lambda i:(i-1)//2
heap_left = lambda i:i*2+1
heap_right = lambda i:i*2+2


def compare_larger(a,b):
    return a>b


def compare_larger_or_equal(a,b):
    return a>=b


def compare_smaller(a,b):
    return a<b


def compare_smaller_or_equal(a,b):
    return a<=b

class Heap(object):

    def __init__(self, array, compare):
        super(Heap, self).__init__()
        self.cmp = compare
        self._tree = list(array)
        if array:
            self._heapify()



    def _heapify(self):
        size = len(self)
        for i in range(size//2-1, -1, -1):
            self._shiftdown(i)


    def add(self, elem):
        self._tree.append(elem)
        self._shiftup(len(self)-1)


    def extract(self):
        if self.is_empty():
            return None
        tree = self._tree
        elem = tree[0]
        end_elem = tree.pop()
        if tree:
            tree[0] = end_elem
            self._shiftdown(0)
        return elem


    def _shiftup(self, index):
        tree = self._tree
        elem = tree[index]
        pindex = heap_parent(index)
        while index>0 and \
            self.cmp(elem, tree[pindex]):
                tree[index] = tree[pindex]
                index = pindex
                pindex = heap_parent(index)
        tree[index] = elem


    def _shiftdown(self, index):
        tree = self._tree
        elem = tree[index]
        size = len(self)
        shift_to = heap_left(index)
        while shift_to<size:
            if shift_to+1<size and \
                self.cmp(tree[shift_to+1], tree[shift_to]):
                    shift_to += 1
            if self.cmp(elem, tree[shift_to]):
                break
            tree[index] = tree[shift_to]
            index = shift_to
            shift_to = heap_left(index)
        tree[index] = elem


    def is_empty(self):
        return len(self)==0


    def top(self):
        if not self.is_empty():
            return self._tree[0]


    def __str__(self):
        return f"size:{len(self)}\n{self._tree}"


    def __repr__(self):
        return f"{self.__class__} at {id(self)}"


    def __len__(self):
        return len(self._tree)


class MaxHeap(Heap):
    def __init__(self,array=[], compare=compare_larger_or_equal):
        super(MaxHeap, self).__init__(array, compare)


class MinHeap(Heap):
    def __init__(self, array=[], compare=compare_smaller_or_equal):
        super(MinHeap, self).__init__(array,compare)