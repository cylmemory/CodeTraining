# 空间复杂度o(n):需要辅助空间是n
# 时间复杂度o(nlogn):归并log2n+1,比较次数:n,因此为nlogn


def merge_sort(slist):
    if len(slist) > 1:
        mid = len(slist)//2
        llist = slist[:mid]  # 二路归并左边
        rlist = slist[mid:]  # 二路归并右边

        merge_sort(llist)
        merge_sort(rlist)

        l, r, k = 0, 0, 0

        while l < len(llist) and r < len(rlist):
            if llist[l] < rlist[r]:
                slist[k] = llist[l]
                l += 1
            else:
                slist[k] = rlist[r]
                r += 1
            k += 1

        while l < len(llist):  # 左边剩余的
            slist[k] = llist[l]
            l += 1
            k += 1

        while r < len(rlist):  # 右边剩余的
            slist[k] = rlist[r]
            r += 1
            k += 1

        return slist


test1 = [4, 9, 3, 1, 2]
test2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print(merge_sort(test1))
print(merge_sort(test2))
