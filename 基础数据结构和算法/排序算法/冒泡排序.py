def bubble_sort(alist):
    if alist == [] or alist is None:
        return
    for i in range(0, len(alist)):
        for j in range(1, len(alist)-i):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
    return alist

test = [3, -3, 1, 10, 5, 0, 4]
print(bubble_sort(test))