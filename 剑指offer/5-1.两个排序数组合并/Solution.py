# 题目描述：
# 有两个排序数组A1和A2，内存在A1的末尾有足够多的空余空间容纳A2，实现一个函数，把A2 插入到A1，并且是有序的
# 思路：本题和第5题思路基本一样，合并两个数据，最好第办法就是从尾部到头部到顺序进行比较元素，并把大的元素一次放在尾部
class Solutuon:
    def merge_arr(self,arr_A1, arr_A2, len_A1, len_A2):
        len_all = len_A1 + len_A2 -1
        arrAll = (len_all+1) * [None]
        index_A1 = len_A1 - 1
        index_A2 = len_A2 - 1

        while index_A1 >= 0 and index_A2 >= 0:
            if arr_A1[index_A1] >= arr_A2[index_A2]:
                arrAll[len_all] = arr_A1[index_A1]
                len_all -= 1
                index_A1 -= 1
            else:
                arrAll[len_all] = arr_A2[index_A2]
                len_all -= 1
                index_A2 -= 1

        while index_A1 >= 0:
            arrAll[len_all] = arr_A1[index_A1]
            len_all -= 1
            index_A1 -= 1
        while index_A2 >= 0:
            arrAll[len_all] = arr_A2[index_A2]
            len_all -= 1
            index_A2 -= 1
        return arrAll

s = Solutuon()
print(s.merge_arr([1, 2, 3, 5], [2, 3, 4, 5], 4, 4)) # [1, 2, 2, 3, 3, 4, 5, 5]
