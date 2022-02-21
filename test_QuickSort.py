#coding:utf-8
from random import randint

from QuickSort import quicksort



if __name__ == '__main__':
    print("升序")
    s=[randint(0,1000) for _ in range(50)]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[1,1,1,1]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[1,2,3,4,5]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[1]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[]
    right_sort=sorted(s)
    quicksort(s)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    print("降序")
    s=[randint(0,1000) for _ in range(50)]
    right_sort=sorted(s,reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[1,1,1,1]
    right_sort=sorted(s, reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[5,4,3,2,1]
    right_sort=sorted(s, reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[1]
    right_sort=sorted(s, reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[]
    right_sort=sorted(s, reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")

    s=[]
    right_sort=sorted(s, reverse=True)
    quicksort(s,True)
    if s!=right_sort:
        print(s)
        print(right_sort)
        print("sort worse")