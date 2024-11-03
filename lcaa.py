class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findPath(root, path, k):
    if root is None:
        raise EnvironmentError

    if root.data == k:
        return True
    
    path.append(root.data)

    if ((root.left != None) and (findPath(root.left, path, k))) or ((root.right != None) and (findPath(root.right, path, k))):
        return True 
    
    path.pop()
    return False 


def lca(root, node1, node2):
    
    path1, path2 = [], []
    if not root:
        return 0
#    left_result = lca(root.left, node1, node2)

    if (not findPath(root, path1, node1) or not findPath(root, path2, node2)):
        return -1
    
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]




def dfs(root, node):
    if root == None:
        return False
    
    if root.data == node.data:
        return True
    
    if ((root.left != None) and dfs(root.left, node)) or (root.right != None and dfs(root.right, node)):
        return True
    return False

def dfs2(root, node):
    if root == None:
        return False
    
    s = []
    s.append(root)
    while s:
        v = s.pop()

        if v.data == node.data:
            return True
        if v.left != None:
            s.append(v.left)
        
        if v.right != None:
            s.append(v.right)
    return False





def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(dfs(root, Node(7)))
    print(dfs(root, Node(1)))
    print(dfs(root, Node(15)))
    print()
    print(dfs2(root, Node(7)))
    print(dfs2(root, Node(1)))
    print(dfs2(root, Node(21)))
    print()

    x = lca(root, 4,5)
    #print('the lca of 4, 5 is ' + str(x))
    y = lca(root, 6, 7)
    #print('the lca of 6, 7 is ' + str(y))
    z = lca(root, 2, 3)
    #print('the lca of 2, 3 is ' + str(z))
    print()
    w = lca(root, 3, 4)
    #print('the lca of (4, 3) is ' + str(w))



if __name__ == "__main__":
    main()