class Solution:
    def restoreIpAddresses(self, s: str):
        if len(s) < 4:
            return []
        answer = set()
        self.helper(s, 1, 3, 5, answer)
        return list(answer)
    def helper(self, s, dot1, dot2, dot3, answer):
        original_string = [x for x in s]
        original_string.insert(dot1, ".")
        original_string.insert(dot2, ".")
        original_string.insert(dot3, ".")
        if "".join(original_string) not in answer:
            if original_string[-1] == ".":
                return
            separated_strings = "".join(original_string).split(".")
            flag = 0
            for x in separated_strings:
                if len(x) <= 0 or int(x) > 255:
                    flag = 1
                elif len(x) > 1 and int(x[0]) == 0:
                    flag = 1
            if flag == 0:
                answer.add("".join(original_string))
            one, two, three, four = separated_strings
            if one != "" and int(one) < 255:
                self.helper(s, dot1+1, dot2, dot3, answer)
            if two != "" and int(two) < 255:
                self.helper(s, dot1, dot2+1, dot3, answer)
            if three != "" and int(three) < 255:
                self.helper(s, dot1, dot2, dot3+1, answer)