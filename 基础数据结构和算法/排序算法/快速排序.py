# coding: utf-8
# 空间复杂度o(logn):
# 时间复杂度o(nlogn),最坏的情况是n^2
def quickSort(slist):
    if slist == [] or slist is None:
        return
    help(slist, 0, len(slist)-1)


def help(slist, start, end):
    if start < end:
        position = partition(slist, start, end)

        help(slist, start, position-1)  # 左子数组递归
        help(slist, position+1, end)  # 右子数组递归


# 切分为两个子数组
def partition(slist, start, end):
    pivotvlue = slist[start]
    left_mark = start + 1
    right_mark = end

    done = False

    while not done:
        while left_mark <= right_mark and slist[left_mark] <= pivotvlue:  # 数组左边与基准元素pivotvlue比较
            left_mark += 1
        while left_mark <= right_mark and slist[right_mark] >= pivotvlue:  # 数组右边与基准元素pivotvlue比较
            right_mark -= 1

        if left_mark > right_mark:
            done = True
        else:
            slist[left_mark], slist[right_mark] = slist[right_mark], slist[left_mark]

    slist[start], slist[right_mark] = slist[right_mark], slist[start]  # 左边小和右边大分组之后，把start位置的和新的基准位置调换位置

    return right_mark  # 返回基准的位置


test_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
test_data1 = [1]
quickSort(test_data)
quickSort(test_data1)
print(test_data)
print(test_data1)