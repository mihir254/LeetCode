class Solution:
    def minProductSum(self, nums1, nums2) -> int:
        temp1, temp2 = [0]*102, [0]*102
        for i in range(len(nums1)):
            temp1[nums1[i]] += 1
            temp2[nums2[i]] += 1
        i, j, sumo = 1, 100, 0
        while i<101 and j>0:
            while temp1[i]==0 and i<101:
                i+=1
            while temp2[j]==0 and j>0:
                j-=1
            sumo += i*j
            if i == 101 or j == 0:
                return sumo
            temp1[i] -= 1
            temp2[j] -= 1
        return sumo