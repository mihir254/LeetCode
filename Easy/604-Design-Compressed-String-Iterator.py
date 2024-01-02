class StringIterator:

    def __init__(self, compressedString: str):
        self.dq = []
        i = 0
        number = 0
        while i < len(compressedString):
            if (compressedString[i]).isnumeric():
                number *= 10
                number += int(compressedString[i])
            else:
                if number != 0:
                    self.dq.append(number)
                    number = 0
                self.dq.append(compressedString[i])
            i += 1
        if number > 0:
            self.dq.append(number)

    def next(self) -> str:
        if not self.dq:
            return ' '
        letter = self.dq.pop(0)
        iterator = self.dq.pop(0)
        newIterator = iterator - 1
        if newIterator > 0:
            self.dq.insert(0, newIterator)
            self.dq.insert(0, letter)
        return letter

    def hasNext(self) -> bool:
        return True if self.dq else False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()