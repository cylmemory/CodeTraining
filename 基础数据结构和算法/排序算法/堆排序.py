def adjust_heap(slist, i, len_list):

    k = 2 * i + 1
    while k < len_list:
        if k+1 < len_list and slist[k] < slist[k+1]:
            k += 1
        if slist[i] < slist[k]:
            slist[i], slist[k] = slist[k], slist[i]
            k = 2 * k + 1
        else:
            break


def heap_sort(slist):
   if slist == [] or slist is None:
       return

   i = len(slist)//2-1
   while i >= 0:
       adjust_heap(slist, i, len(slist))    # 构建大堆
       i -= 1

   k = len(slist)-1
   while k > 0:
       slist[0], slist[len(slist)-1] = slist[len(slist)-1], slist[0]
       adjust_heap(slist, 0, len(slist)-1)   # 堆顶和末尾元素交换 and 调整堆结构
       k -= 1
   return slist


test=[49, 38, 65, 97, 76, 13, 27, 49]

print(heap_sort(test))
