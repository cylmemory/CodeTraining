class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        if self.queue2 == []:
            self.queue1.append(data)
        else:
            self.queue2.append(data)

    def pop(self):
        if self.queue1 == [] and self.queue2 == []:
            return
        if self.queue1 != []:
            length = len(self.queue1)
            for i in range(length-1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            length = len(self.queue2)
            for i in range(length-1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop()) # 1
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
