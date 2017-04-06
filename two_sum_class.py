class Two_Sum(object):
    def __init__(self):
        self.nums = {}

    def add(self, num):
        if num in self.nums:
            cnt = self.nums[num] + 1
            self.nums[num] = cnt
        else:
            self.nums[num] = 1

    def find(self, target):
        for x in self.nums.keys():
            val = target - x
            if val in self.nums:
                return True
        return False


if __name__ == '__main__':
    two_sum = Two_Sum()
    two_sum.add(1)
    two_sum.add(3)
    two_sum.add(5)
    two_sum.add(3)
    two_sum.add(5)
    print(two_sum.find(4))
    print(two_sum.find(7))
    print(two_sum.find(10))
    print(two_sum.find(17))
    print(two_sum.find(1))
    print(two_sum.find(6))
    print(two_sum.find(8))
