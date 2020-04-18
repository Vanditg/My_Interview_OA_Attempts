class Node:
  	def __init__(self, val):
      	self.val = val
        self.left = None
        self.right = None
        self.parent = None

def get_leaves(node, leaves):
  	if node is None:
      	return
    
    if node.left is None and node.right is None:
      	leaves.append(node)
        return
    
    get_leaves(node.left, leaves)
    get_leaves(node.right, leaves)
    return        

def dfs(node, distance, k, leaves, visited, pairs):
  	if node is None or node in visited:
      	return None
    
    if distance > k:
      	return None
    
    if node in leaves and distance <= k:
      	pairs.append(node)
    
    distance += 1
    visited.add(node)
    dfs(node.parent, distance, k, leaves, visited, pairs)
    dfs(node.left, distance, k, leaves, visited, pairs)
    dfs(node.right, distance, k, leaves, visited, pairs)
    return


k = int(stdin.readline().strip())
height = int(stdin.readline().strip())
root_val = int(stdin.readline().strip())
root = Node(root_val)
queue = [root]
for _ in range(height):
  	n = len(queue)
    children = stdin.readline().strip().split()
    for i in range(n):
      	node = queue.pop(0)
        left_val = children[2*i]
        right_val = children[(2*i) +1]
        if left_val != -1:
          	left_child = Node(left_val)
            node.left = left_child
            left_child.parent = node
            queue.append(left_child)
        if right_val != -1:
          	right_child = Node(right_val)
            node.right = right_child
            right_child.parent = node
            queue.append(right_child)

leaves = []
get_leaves(root, leaves)
result = set()
for leaf in leaves:
	visited = set()
    pairs = []
    dfs(leaf, 0, k, leaves, visited, pairs)
    for node in pairs:
      	if (leaf, node) in result or (node, leaf) in result:
          	continue
        else:
          	result.add((leaf, node))

print(len(result))      
