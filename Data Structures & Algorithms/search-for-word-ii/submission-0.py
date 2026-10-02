class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = None
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                
                node = node.children[ch]
            
            node.isEnd = True
            node.word = word
        
        rows, cols = len(board), len(board[0])

        results = []
        def dfs(r, c, node):
            if ( r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "#"):
                return
            
            ch = board[r][c]

            if ch not in node.children:
                return
            
            next_node = node.children[ch]
            if next_node.isEnd:
                results.append(next_node.word)

                next_node.isEnd = False
            
            temp = board[r][c]
            board[r][c] = "#"
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)

        return results