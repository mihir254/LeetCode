class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split("/")
        ans = []
        for i in a:
            if i == ".":
                continue
            if i == "..":
                if ans:
                    ans.pop()
            else:
                if i:
                    ans.append(i)
        return "/" + "/".join(ans) if ans else "/"