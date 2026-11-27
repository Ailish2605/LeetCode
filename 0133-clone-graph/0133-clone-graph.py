"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Graph traversal O(V+E)

        #Seen data structure
        oldToNew = {}
        #Use recursion
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            #Create copy of the current node
            new_node = Node(node.val)
            oldToNew[node] = new_node
            
            #For each neighbor recursively create it, add to list
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        if not node:
            return None
        return dfs(node)
    
    
    
        
        
        