# 题目描述：
# 将一个字符串中的空格替换成 "%20"
# 要求是时间复杂度 O(N)，空间复杂度 O(1)
# example:
# Input:
# "A B"
#
# Output:
# "A%20B"
# 思路:
# 1.先遍历字符串有空格符，如果要更换成"%20"，需要在尾部填充两个任意字符。
# 2.令P1 指向字符串原来的末尾位置，P2 指向字符串现在的末尾位置，
# P1 和 P2 从后向前遍历，当 P1 遍历到一个空格时，就需要令 P2 指向的位置依次填充 02%，否则就填充上 P1 指向字符的值

class Solution:
    def replaceBlank(self, init_str):

        if not isinstance(init_str, str) or len(init_str) <= 0 or init_str == None:
            return ""

        blank_nums = 0
        for i in init_str:
            if i == " ":
                blank_nums += 1
        init_str_len = len(init_str)
        new_str_len = init_str_len + blank_nums*2
        new_str = new_str_len * [None]
        init_str_index, new_str_index = init_str_len-1, new_str_len-1

        while init_str_index >= 0 and new_str_index >= init_str_index:
            if init_str[init_str_index] == " ":
                new_str[new_str_index-2:new_str_index+1] = ['%', '2', '0']
                new_str_index -= 3
                init_str_index -= 1
            else:
                new_str[new_str_index] = init_str[init_str_index]
                new_str_index -= 1
                init_str_index -= 1
        return "".join(new_str)


s = ''
test = Solution()
print(test.replaceBlank(s))