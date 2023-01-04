class Solution:
    def minDeletionSize(self, strs) -> int:
        length = len(strs[0])
        indexedString = [""]*length
        print(indexedString)
        for string in strs:
            for index in range(length):
                indexedString[index] += string[index]
        count = 0
        for string in indexedString:
            for index in range(len(string)-1):
                if ord(string[index+1]) - ord(string[index]) < 0:
                    count += 1
                    break
        return count