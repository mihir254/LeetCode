class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ab, bb, cb = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        maxlen = max(len(ab), len(bb), len(cb))
        aadd, badd, cadd = maxlen-len(ab), maxlen-len(bb), maxlen-len(cb)
        ab = ''.join(['0']*aadd + [x for x in ab])
        bb = ''.join(['0']*badd + [x for x in bb])
        cb = ''.join(['0']*cadd + [x for x in cb])
        count = 0
        for i in range(maxlen):
            if cb[i] == '1':
                if ab[i] == '0' and bb[i] == '0':
                    count += 1
            else:
                if ab[i] == '1' and bb[i] == '1':
                    count += 2
                elif ab[i] == '1' or bb[i] == '1':
                    count += 1
        return count