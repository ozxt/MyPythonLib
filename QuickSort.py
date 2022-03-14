#coding:utf8

from random import randint


def quicksort(arr, reverse=False):
    """ 快速排序
    对arr原地进行快速排序

    :param arr: 待排数组
    :param reverse: 默认升序,置True为降序
    """
    # _quicksort(arr,0,len(arr)-1,reverse)
    _quicksort_equal_aggregation(arr,0,len(arr)-1,reverse)

def _quicksort(arr, left, right, reverse):
    if right-left+1 <=16:
        insert_sort(arr, left, right, reverse)
        return
    if left<right:
        mid = _partition(arr,left,right,reverse)
        _quicksort(arr, left, mid-1, reverse)
        _quicksort(arr, mid+1, right, reverse)

def _partition(arr,left, right, reverse):
    cmp = (lambda a,b: a<=b) if reverse else (lambda a,b: a>=b)
    i = randint(left, right)
    arr[left],arr[i] = arr[i], arr[left]
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


def insert_sort(arr, left, right, reverse=False):
    cmp = (lambda a,b: a<b) if reverse else (lambda a,b: a>b)
    i = left+1
    while i<=right:
        tmp = arr[i]
        j = i-1
        while j>=left and cmp(arr[j], tmp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
        i += 1

def _quicksort_equal_aggregation(arr, left, right, reverse):
    if left<right:
        if right-left+1 <=16:
            insert_sort(arr, left, right, reverse)
            return
        else:
            agg_left,agg_right = _partition_equal_aggregation(
                                        arr,left,right,reverse )
            _quicksort_equal_aggregation(arr, left, agg_left-1, reverse)
            _quicksort_equal_aggregation(arr, agg_right+1, right, reverse)


def _partition_equal_aggregation(arr,left, right, reverse):
    """用于快排的切分函数
    不同之处在于它将所有的与切分元素pivot相等的元素聚集在中间

    :returns: pivot聚合区间的左右边界
    :rtype: (int,int)
    """
    cmp = (lambda a,b: a<b) if reverse else (lambda a,b: a>b)
    i = randint(left, right)
    arr[left],arr[i] = arr[i], arr[left]
    pivot = arr[left]
    # 把和pivot相等的聚集在一起,使：
    # arr[left,L-1] < pivot
    # arr[L,R] == pivot
    # arr[R+1,right] > pivot

    # left L-->  i-->遍历   <--R right
    i = left+1
    L = left
    R = right+1
    while i<R:
        if cmp(arr[i],pivot):
            R-=1
            arr[i],arr[R] = arr[R], arr[i]
        elif arr[i]==pivot:
            i+=1
        else:
            L+=1
            arr[i],arr[L] = arr[L], arr[i]
            i+=1
    # arr[left]没变过，一直是pivot
    # 最后L要么没动过就在left处，要么它指向的元素一定符合
    # arr[L]<pivot (升序) 或 # arr[L]>pivot (降序)
    arr[L],arr[left] = arr[left],arr[L]
    # 经过最后一次交换，L处变成pivot，
    # R还在>pivot（升序）或<pivot(降序)的边界上
    R -= 1
    return L,R


