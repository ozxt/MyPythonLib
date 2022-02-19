#coding:utf8

def compare_larger(a,b):
    return a>b


def compare_larger_or_equal(a,b):
    return a>=b


def compare_smaller(a,b):
    return a<b


def compare_smaller_or_equal(a,b):
    return a<=b

def quicksort(arr,cmp=compare_larger_or_equal):
    _quicksort(arr,0,len(arr)-1,cmp)

def _quicksort(arr, left, right, cmp):
    if left<right:
        mid = _partition(arr,left,right,cmp)
        _quicksort(arr, left, mid-1, cmp)
        _quicksort(arr, mid+1, right, cmp)

def _partition(arr,left, right, cmp):
    # 暂存arr[left]，区间最左端这个位置就空出来了
    pivot = arr[left]
    while left<right:
        # 先从区间右端开始，找到一个不符合顺序的元素，将它放到left位置，
        # 这样当前的right位置就空出来了
        while left<right and cmp(arr[right],pivot):
            right-=1
        if left==right:
            break
        arr[left] = arr[right]
        left+=1
        # 再从区间左端开始，找到一个不符合顺序的元素，将它放到right位置
        # 这样当前的left位置就空出来了
        while left<right and cmp(pivot, arr[left]):
            left+=1
        if left==right:
            break
        arr[right] = arr[left]
        right-=1
    # 循环左右，left和right终会相遇
    # 此时的left位置（空出来了）就可以放下pivot
    # 这个值也就确定了在最终排序里的位置
    arr[left] = pivot
    return left
