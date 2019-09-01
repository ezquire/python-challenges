class Node:
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
    
def findPath(root, path, node):
    if not root: 
        return False
        
    path.append(root)
    
    if root.key == node.key: 
        return True
          
    if findPath(root.left, path, node) or findPath(root.right, path, node): 
        return True
        
    path.pop()
    return False
    
def lca1(root, node1, node2): 
    path1 = []
    path2 = []
    
    if not findPath(root, path1, node1) or not findPath(root, path2, node2):
        return -1
        
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]
    
def lca2(node1, node2):
    nodes = set()
    while node1:
        nodes.add(node1)
        node1 = node1.parent
    
    while node2:
        if node2 in nodes:
            return node2
        nodes.add(node2)
        node2 = node2.parent
        
def lca3(node1, node2):
    temp1 = node1
    temp2 = node2
    height1, height2 = 0, 0
    
    while temp1:
        height1 += 1
        temp1 = temp1.parent
    
    while temp2:
        height2 += 1
        temp2 = temp2.parent
        
    while height1 != height2:
        if height1 < height2:
            node2 = node2.parent
            height2 -= 1
        if height2 < height1:
            node1 = node1.parent
            height1 -= 1
    
    while node1 and node2:
        if node1 == node2: 
            return node1
        node1 = node1.parent
        node2 = node2.parent
        
root = Node(1, None) 
root.left = Node(2, root) 
root.right = Node(3, root) 
root.left.left = Node(4, root.left) 
root.left.right = Node(5, root.left) 
root.right.left = Node(6, root.right) 
root.right.right = Node(7, root.right) 

node2 = root.left       
node3 = root.right  
node4 = root.left.left   
node5 = root.left.right 
node6 = root.right.left 
node7 = root.right.right

print(lca1(root, node4, node5).key)
print(lca2(node4, node5).key)
print(lca3(node4, node5).key)
