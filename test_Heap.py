#coding:utf-8
from Heap import MaxHeap

class A:
    def __init__(self,a):
        self.elem1 = a
        self.elem2 = [1,2,3]
        self.elem3 = {1:'asdasd'}

    def __repr__(self):
        return f"elem1:{self.elem1}"


def compare(a,b):
    return a.elem1 >= b.elem1

if __name__ == '__main__':
    # s=[1,5,3,2,9,7]
    # maxheap = MaxHeap(s)
    s=[A(23),A(3),A(76),A(1)]
    maxheap = MaxHeap(s,compare)
    print(repr(maxheap))
    print(maxheap)
    # maxheap = MaxHeap()
    # s=[1,5,3,9,7,2,1,2,4,2,1,4,2]
    # print(s)
    # for i in s:
    #     maxheap.add(i)

    # print(repr(maxheap))
    # print(maxheap)

    # while not maxheap.is_empty():
    #     print(maxheap.extract())