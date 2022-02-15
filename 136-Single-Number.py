class Solution:
    def singleNumber(self, nums) -> int:
        # array = []
        # for i in nums:
        #     if i not in array:
        #         array.append(i)
        #     else:
        #         array.remove(i)
        # return array[0]
        temp = 0
        for i in nums:
            temp ^= i
        return temp