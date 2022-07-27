class Solution:
    def getMaxLen(self, nums) -> int:
        # Brute force
        # maxi = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)+1):
        #         subarray = nums[i:j]
        #         prod = subarray[0]
        #         for k in range(1, len(subarray)):
        #             prod *= subarray[k]
        #         if prod > 0:
        #             maxi = max(maxi, len(subarray))
        # return maxi
        possible_answers = []
        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i > start:
                    possible_answers.append(nums[start:i])
                start = i+1
        if start < len(nums):
            possible_answers.append(nums[start:])
        maxi = 0
        for each in possible_answers:
            negs, first_neg, last_neg = 0, -1, -1
            for i in range(len(each)):
                if each[i] < 0:
                    if negs == 0:
                        first_neg = i
                    negs += 1
                    last_neg = i
            if negs%2==0:
                maxi = max(maxi, len(each))
            else:
                maxi = max(maxi, len(each[first_neg+1:]), len(each[:last_neg]))
        return maxi