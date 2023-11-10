from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res
        
        queue = deque([root])
        level = 1
        
        while queue:
            level_values = []
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if level % 2 == 0:
                level_values.reverse()
                
            res.append(level_values)
            level += 1
        
        return res
