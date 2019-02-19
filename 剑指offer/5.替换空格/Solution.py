class Solution:
    def replaceSpace(self, example):

        if example == None or len(example) == 0 or not isinstance(example, str):
            return ""

        str_len = len(example)
        space_nums = 0
        for i in example:
            if i == " ":
                space_nums += 1

        new_str_len = str_len + space_nums*2
        new_str = new_str_len * [None]

        indexInitial, indexNew = str_len-1, new_str_len-1

        while indexInitial >= 0 and indexNew >= indexInitial:
            if example[indexInitial] == '':
                new_str[indexNew-2:indexNew+1] = ['%', '2', '0']
                indexInitial -= 1
                indexNew -= 3
            else:
                new_str[indexNew] = example[indexInitial]
                indexNew -= 1
                indexInitial -= 1
        return "".join(new_str)


s = 'we are happy'
test = Solution()
print(test.replaceSpace(s))