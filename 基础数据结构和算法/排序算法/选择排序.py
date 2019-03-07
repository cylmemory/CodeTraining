# 空间复杂度o(1)
# 时间复杂度o(n^2):(n-1)+(n-2)+...1=n*(n-1)/2


def selection_sort(alist):
    if alist == [] or alist is None:
        return
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


test = [9, -1, 3, 10, 5, 0, -10, 8]
print(selection_sort(test))