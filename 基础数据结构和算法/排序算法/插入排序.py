# 空间复杂度o(1)
# 时间复杂度o(n^2):1+2+3+...(n-1)=n*(n-1)/2


def insert_sort(alist):
    if alist == [] or alist is None:
        return
    for i in range(1, len(alist)):
        x = alist[i]
        j = i
        while j > 0 and alist[j-1] > x:  # 从后面到前面依次比较
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = x
    return alist


test = [4, 1, 9, 3, 11, 5, -1]
print(insert_sort(test))

