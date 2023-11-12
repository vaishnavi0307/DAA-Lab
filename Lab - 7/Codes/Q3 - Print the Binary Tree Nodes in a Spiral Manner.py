## Q3 - PRINTING THE BINARY TREE NODES IN A SPIRAL MANNER

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(nums):
    if not nums:
        return None
    
    root = TreeNode(nums.pop(0))
    queue = [root]
    
    while queue and nums:
        node = queue.pop(0)
        
        left_val = nums.pop(0)
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        
        if nums:
            right_val = nums.pop(0)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    
    return root

def spiral_traversal(root):
    if not root:
        return []
    
    result = []
    level = 1
    queue = [root]
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            
            if level % 2 == 1:
                level_nodes.append(node.val)
            else:
                level_nodes.insert(0, node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.extend(level_nodes)
        level += 1
    
    return result

# Input list
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Build the binary tree
root = build_tree(input_list)

# Perform spiral traversal
output = spiral_traversal(root)

# Print the result
print(output)
