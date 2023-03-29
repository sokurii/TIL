'''
알고리즘

quick_sort(lst[], left, right)
    if left < right:
        s = partition(a, left, right)
        quick_sort(lst[], left, s-1)
        quick_sort(lst[], s+1, right)

'''

