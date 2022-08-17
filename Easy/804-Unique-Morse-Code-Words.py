class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store = {}
        for word in words:
            mcode = ''
            for letter in word:
                mcode += code[ord(letter)-ord('a')]
            if mcode not in store:
                store[mcode] = 0
        cnt = 0
        for k, v in store.items():
            cnt += 1
        return cnt