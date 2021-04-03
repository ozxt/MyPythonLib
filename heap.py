heap_parent = lambda i:(i-1)//2
heap_left = lambda i:i*2+1
heap_right = lambda i:i*2+2

def compare_larger(a,b):
    if a>b:
        return 1
    if a==b:
        return 0
    return -1

def compare_smaller(a,b):
    if a>b:
        return -1
    if a==b:
        return 0
    return 1


class Heap(object):
    def __init__(self, compare):
        super(Heap, self).__init__()
        self.size = 0
        self.tree = []
        self.cmp = compare

    def insert(self, data):
        self.tree.append(data)
        ipos = self.size
        ppos = heap_parent(ipos)
        tmp = self.tree[ipos]
        while ipos>0:
            if self.cmp(tmp, self.tree[ppos]) == 1:
                self.tree[ipos] = self.tree[ppos]
                ipos = ppos
                ppos = heap_parent(ipos)
            else:
                break
        self.tree[ipos] = tmp
        self.size += 1


    def extract(self):
        if self.size == 0:
            return None

        data = self.tree[0]
        self.size -= 1
        if self.size == 0:
            self.tree = []
            return data
        self.tree[0] = self.tree[self.size]
        self.tree.pop()
        ipos = 0
        while ipos < self.size:
            left = heap_left(ipos)
            right = heap_right(ipos)
            if left < self.size and self.cmp(self.tree[ipos],self.tree[left]) == -1:
                mpos = left
            else:
                mpos = ipos

            if right < self.size and self.cmp(self.tree[mpos], self.tree[right]) == -1:
                mpos = right

            if mpos == ipos:
                break
            else:
                self.tree[ipos], self.tree[mpos] = self.tree[mpos], self.tree[ipos]
                ipos = mpos

        return data

    def extract_iter(self):
        while not self.is_empty():
            yield self.extract()

    def is_empty(self):
        return self.size==0

    def __repr__(self):
        return f"size:{self.size}\n{self.tree}"

class MaxHeap(Heap):
    def __init__(self,compare=compare_larger):
        super(MaxHeap, self).__init__(compare)


class MinHeap(Heap):
    def __init__(self, compare=compare_smaller):
        super(MinHeap, self).__init__(compare)