__author__ = "Vishal Garg(vg3660)"
"""
    The MergeSort modified for objects of type LaserPoint
"""
def mergeSort(list):
    if 1>=len(list):
        return list[:]
    mid=len(list)//2
    left=mergeSort(list[:mid])
    right=mergeSort(list[mid:])
    lf=0
    rf=0
    result=[]
    while lf<len(left) and rf<len(right):
        if left[lf].score>right[rf].score:
            result.append(left[lf])
            lf+=1
        else:
            result.append(right[rf])
            rf+=1
    if lf<len(left):
        result.extend(left[lf:])
    else:
        result.extend(right[rf:])

    return result