class Solution:
    def maxLength(self, arr):
        return self.recursion(arr, "", -1)
        
    def recursion(self, words, curStr, maxi):
        if len(curStr) != len(set(curStr)):
            return -1
        if not words:
            return len(curStr)
        max1 = max(maxi, self.recursion(words[1:], curStr, maxi))
        max2 = max(maxi, self.recursion(words[1:], curStr+words[0], maxi))
        return max(max1, max2)