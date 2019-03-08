# 空间复杂度o(1)
# 时间复杂度o(n^2):1+2+3+...(n-1)=n*(n-1)/2


def bubble_sort(alist):
    if alist == [] or alist is None:
        return
    for i in range(0, len(alist)):
        for j in range(1, len(alist)-i):  # 1到len(alist)-i是为了顶部元素排除比较
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
    return alist


test = [3, -3, 1, 10, 5, 0, 4]
print(bubble_sort(test))


# 改进版本：设置要个found在外部循环，当内部循环中元素当位置没有发生改变时，就可以认定改数组为有序，接着跳出循环，返回数组
def bubble_sort2(alist):
    if alist == [] or alist is None:
        return

    for i in range(len(alist)):
        found = False

        for j in range(1, len(alist)-i):
            if alist[j-1] > alist[j]:
                alist[j-1], alist[j] = alist[j], alist[j-1]
                found = True
        if not found:
            break
    return alist


test1 = [1, 2, 3, 4, 5, 6, 7]
test2 = [3, 1, 9, 2, -1, 4, -9]

print(bubble_sort2(test1))
print(bubble_sort2(test2))