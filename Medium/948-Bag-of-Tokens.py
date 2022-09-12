class Solution:
    def bagOfTokensScore(self, tokens, power):
        score, high = 0, 0
        tokens.sort()
        while tokens:
            if score == 0 and power < tokens[0]:
                return 0
            while tokens and power >= tokens[0]:
                power -= tokens.pop(0)
                score += 1
            high = max(high, score)
            if tokens and score > 0:
                score -= 1
                power += tokens.pop()
        return high