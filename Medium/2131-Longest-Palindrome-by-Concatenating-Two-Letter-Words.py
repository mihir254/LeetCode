class Solution:
    def longestPalindrome(self, words) -> int:
        store1, store2 = {}, {}
        for word in words:
            if word[0] == word[1]:
                if word not in store2:
                    store2[word] = 0
                store2[word] += 1
            else:
                if word in store1:
                    store1[word][0] += 1
                elif word[::-1] in store1:
                    store1[word[::-1]][2] += 1
                else:
                    store1[word] = [1, word[::-1], 0]
        count = 0
        for key, val in store1.items():
            count += min(val[0], val[2])*4
        odd = False
        for key, val in store2.items():
            can_add = val//2
            count += can_add*4
            if val%2!=0 and not odd:
                odd = True
        return count if not odd else count+2