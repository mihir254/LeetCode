class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i, j = 0, 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
        if (len(nums))%2==1:
            return nums[len(nums)//2]
        else:
            return (nums[(len(nums)//2)-1]+nums[(len(nums)//2)])/2