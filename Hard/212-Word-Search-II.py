from typing import List
class TreeNode:
    def __init__(self):
        self.children = {}
        self.isLast = False

class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            node = node.children[ch]
        node.isLast = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        answer = []
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, visited, answer, '', trie.root)
        return answer
    def dfs(self, x, y, matrix, visited, answer, path, node):
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] not in node.children:
            return
        node = node.children[matrix[x][y]]
        if node.isLast:
            answer.append(path+matrix[x][y])
            node.isLast = False
        visited.add((x, y))
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for (nx, ny) in neighbours:
            if (x+nx, y+ny) not in visited:
                self.dfs(x+nx, y+ny, matrix, visited, answer, path+matrix[x][y], node)
        visited.remove((x, y))