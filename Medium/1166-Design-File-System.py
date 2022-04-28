class FileSystem:

    def __init__(self):
        self.store = {}

    def createPath(self, path: str, value: int) -> bool:
        path_divs = path.split("/")[1:]
        if path in self.store:
            return False
        elif len(path_divs) == 1:
            self.store[path] = value
            return True
        else:
            parent = "/" + "/".join(path_divs[:-1])
            if parent in self.store:
                self.store[path] = value
                return True
            return False
            

    def get(self, path: str) -> int:
        if path in self.store:
            return self.store[path]
        return -1