# Sort Array By Parity
# 题目大意：
# 给出一个非负整数的数组A，返回一个由A的所有偶数元素组成的数组，后跟A的所有奇数元素
# 例如：Input: [3,1,2,4]
#      Output: [2,4,3,1]
#      The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
# 题目解析：
# 一般都是要先判断数组中的元素为奇偶数，然后进行排序，如方法1，
# 要么就是使用首尾指针指向的元素进行判断奇偶性，再交换位置进行排序，如方法2
# 再者，使用python自带的sorted函数，如方法3

# 方法1：简单粗暴，新建两个数组对象存放偶数元素和奇数元素，然后再相加
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []

        for a in A:
            if a % 2 == 0:
                arr1.append(a)
            else:
                arr2.append(a)

        return arr1 + arr2

    # return ([a for a in A if a % 2 == 0] + [b for b in A if b % 2 == 1]) 一行代码实现

    # 时间复杂度：O(N) N代表len(A)
    # 空间复杂度：O(N)

# 方法2：应用快速排序的思想进行对位交换，即需要指向头部和尾部两个指针，判断是否为奇数偶数，然后交换位置
class Solution:
    def sortArrayByParity(self, A):
        s, e = 0, len(A)-1
        while s < e:
            while A[s] % 2 == 0 and s < e:
                s += 1
            while A[e] % 2 == 1 and s < e:
                e -= 1
            A[s], A[e] = A[e], A[s]
        return A
    # 时间复杂度：O(N) N代表len(A)
    # 空间复杂度：O(1)

# 方法3：应用python中sorted函数，这也是最简单且高效率的方法
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key=lambda x: x % 2)
