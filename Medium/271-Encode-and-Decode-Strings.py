from typing import List
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        length = len(strs)
        lengths = [str(len(x)) for x in strs]
        return str(length) + "," + ','.join(lengths) + "," + "".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        separator = s.split(",")
        length = int(separator[0])
        lengths = []
        for i in range(1, length+1):
            lengths.append(int(separator[i]))
        ignoreIndex = len(','.join(separator[:length+1])) + 1
        jointString = s[ignoreIndex:]
        answer = []
        start, end = 0, 0
        for endIndex in lengths:
            start = end
            end = start+endIndex
            thisString = jointString[start:end]
            answer.append(thisString)
        return answer
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))