def bubble_sort(item):
    '''Return array of items, sorted in ascending order'''

    for i in range(len(item)-1,0,-1):

        for j in range(i):

            if item[j]> item[j+1]:

                item[j],item[j+1]=item[j+1],item[j]
    return item


def merge_sort(item):
    if len(item) < 2:
        return item
    result,mid = [],int(len(item)/2)

    n = merge_sort(item[:mid])
    z = merge_sort(item[mid:])

    while (len(n) > 0) and (len(z) > 0):
            if n[0] > z[0]:result.append(z.pop(0))
            else:result.append(n.pop(0))

    result.extend(n+z)
    '''Return array of items, sorted in ascending order'''
    return result


def quick_sort(item):
    if len(item) == 0:
        return item
    pivot = item[0]
    pivots = [i for i in item if i == pivot]
    smaller = quick_sort([i for i in item if i < pivot])
    larger = quick_sort([i for i in item if i > pivot])

    '''Return array of items, sorted in ascending order'''
    return smaller + pivots + larger
