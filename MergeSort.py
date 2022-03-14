#coding:utf8

aux_arr = None

def mergesort(arr, reverse=False):
    """归并排序
    对arr进行原地归并排序

    :param arr: 待排数组
    :param reverse: 默认升序,置True为降序
    """
    global aux_arr
    aux_arr = [0] * len(arr)
    _mergesort(arr, 0, len(arr)-1, reverse)
    aux_arr = None

def _mergesort(arr, left, right, reverse):
    if right-left <= 16:
        insert_sort(arr, left, right, reverse)
    elif left<right:
        mid = left + (right-left)//2
        _mergesort(arr, left, mid, reverse)
        _mergesort(arr, mid+1, right, reverse)
        _merge(arr, left, mid, right, reverse)


def _merge(arr, left, mid, right, reverse):
    """
    把有序区间arr[left,mid]和有序区间arr[mid+1,right]
    合并成有序区间arr[left,right]
    """
    global aux_arr
    cmp = (lambda a,b: a<=b) if reverse else (lambda a,b: a>=b)
    # 把区间复制到辅助数组，在重新排序到arr[left,right]
    for i in range(left, right+1):
        aux_arr[i] = arr[i]
    i,j = left,mid+1
    for k in range(left,right+1):
        if i<=mid and j<=right:
            if cmp(aux_arr[i],aux_arr[j]):
                arr[k] = aux_arr[j]
                j+=1
            else:
                arr[k] = aux_arr[i]
                i+=1
        elif i>mid:
            arr[k] = aux_arr[j]
            j+=1
        elif j>right:
            arr[k] = aux_arr[i]
            i+=1




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


