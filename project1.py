"""
ECE 590
Project 1
Fall 2022
Partner 1:
Partner 2:
Date:
"""

# some helper functions
from project1tests import *


def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp


def findmin(lst, start):
    min = start
    for index in range(start + 1, len(lst)):
        if lst[index] < lst[min]:
            min = index
    return min


def shift_element(lst, old, new):
    lst.insert(new, lst.pop(old))


def find_index(lst, index):
    value = lst[index]
    while index > 0:
        if lst[index - 1] <= value:
            break
        else:
            index -= 1
    return index


def findnextlarge(lst, start, value):
    for i in range(start, len(lst)):
        if lst[i] > value:
            return i
    return -1


"""
SelectionSort
"""


def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        smallest_index = findmin(listToSort, i)
        swap(listToSort, i, smallest_index)
    return listToSort


"""
InsertionSort
"""


def InsertionSort(listToSort):
    for i in range(len(listToSort)):
        index = find_index(listToSort, i)
        shift_element(listToSort, i, index)
    return listToSort


"""
BubbleSort
"""


def BubbleSort(listToSort):
    for i in range(len(listToSort)):
        for j in range(len(listToSort)-i-1):
            if listToSort[j] > listToSort[j+1]:
                listToSort[j], listToSort[j+1] = listToSort[j+1], listToSort[j]
    return listToSort


"""
MergeSort
"""


def merge(lst1, lst2, res):
    i = 0
    j = 0
    res.clear()
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    if i < len(lst1):
        res += lst1[i:]
    if j < len(lst2):
        res += lst2[j:]
    return res


# def MergeSort(arr):
#     if len(arr) > 1:

#         # Finding the mid of the array
#         mid = len(arr)//2

#         # Dividing the array elements
#         L = arr[:mid]

#         # into 2 halves
#         R = arr[mid:]

#         # Sorting the first half
#         MergeSort(L)

#         # Sorting the second half
#         MergeSort(R)

#         i = j = k = 0

#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

def MergeSorthelper(listToSort):
    if len(listToSort) <= 1:
        return listToSort

    mid = len(listToSort)//2
    left = listToSort[:mid]
    right = listToSort[mid:]
    left = MergeSorthelper(left)
    right = MergeSorthelper(right)
    return merge(left, right, listToSort)


def MergeSort(listToSort):

    return MergeSorthelper(listToSort)


"""
QuickSort
Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""


# def QuickSortHelper(lst, res):
#     if len(lst) <= 1:
#         res += lst
#         return
#     i = 1
#     s = 0
# # use mid one as pivot? problem need better way to do that
#     pivot = len(lst) // 2
#     value = lst[pivot]
#     lst.pop(pivot)
#     l = findnextlarge(lst, 0, value)
#     while i < len(lst):
#         if lst[i] <= value:
#             s = i

#         if s > l:
#             l = findnextlarge(lst, l, value)
#             if (l == -1):
#                 break
#             swap(lst, s, l)
#             l, s = s, l
#         i += 1


# #    pivot = s+1
#     if value < lst[s]:
#         pivot = s
#         lst.insert(pivot, value)

#         QuickSortHelper(lst[:pivot+1], res)
#         QuickSortHelper(lst[pivot+1:], res)

#     else:
#         pivot = s+1
#         lst.insert(pivot, value)

#         QuickSortHelper(lst[:pivot], res)
#         QuickSortHelper(lst[pivot:], res)


def QuickSort(listToSort, i=0, j=None):
    # # Set default value for j if None.
    if j == None:
        j = len(listToSort)-1
    # #if i >= j:
    # #    return
    # if i < j:
    #     pivot = QuickSort_helper(listToSort, i, j)

    #     QuickSort(listToSort, i, pivot - 1)
    #     QuickSort(listToSort, pivot + 1, j)

    #     #return listToSort

    QuickSort_helper(listToSort, i, j)
    return listToSort

def QuickSort_helper(listToSort, start, end):

    # # value = listToSort.pop(start)

    # # quick = start
    # # slow = start
    # # while quick < end:
    # #     if listToSort[quick] < value:
    # #         swap(listToSort, quick, slow)
    # #         slow += 1
    # #     quick += 1
    # # listToSort.insert(slow, value)
    # # return slow

    # value = listToSort[end]
    # i = start - 1
    # for j in range(start, end):
    #     if listToSort[j] <= value:
    #         i += 1
    #         listToSort[i], listToSort[j] = listToSort[j], listToSort[i]
    # listToSort[i+1], listToSort[end] = listToSort[end], listToSort[i+1]
    # return i + 1
    if start >= end:
        return
    pivotidx = start
    leftidx = start + 1
    rightidx = end
    while rightidx >= leftidx:
        if listToSort[leftidx] > listToSort[pivotidx] and listToSort[rightidx] < listToSort[pivotidx]:
            swap(listToSort, leftidx, rightidx)
        if listToSort[leftidx] <= listToSort[pivotidx]:
            leftidx += 1
        if listToSort[rightidx] >= listToSort[pivotidx]:
            rightidx -= 1
        swap(listToSort, rightidx, pivotidx)
        leftsmaller = rightidx - 1 - start < end - rightidx - 1
        if leftsmaller:
            QuickSort_helper(listToSort, start, rightidx - 1)
            QuickSort_helper(listToSort, rightidx + 1, end)
        else:
            QuickSort_helper(listToSort, rightidx + 1, end)
            QuickSort_helper(listToSort, start, rightidx - 1)
"""
Importing the testing code after function defs to ensure same references.
"""

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
