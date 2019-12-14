class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def compare(a, b):
    if a is None and b is None:
        return  True

    if a.val != b.val:
        return False

    if a is not None and b is not None:
        return compare(a.left, b.left) and compare(a.right, b.right)

    return  False

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
nodeNone = TreeNode(None)

print(compare(node1, node2))
print(compare(node1, node1))
print(compare(nodeNone, node1))
print(compare(nodeNone, nodeNone))

oneStackRight = TreeNode(1, node1, node2)
oneStackLeft = TreeNode(1, node1, node2)
print(compare(oneStackLeft, oneStackRight))

oneStackRight = TreeNode(1, node1, node3)
oneStackLeft = TreeNode(1, node1, node2)
print(compare(oneStackLeft, oneStackRight))

twoStackRight = TreeNode(1, TreeNode(2, node4, node5), TreeNode(3, node6, node7))
twoStackLeft = TreeNode(1, TreeNode(2, node4, node5), TreeNode(3, node6, node7))
print(compare(twoStackRight, twoStackLeft))

twoStackRight = TreeNode(1, TreeNode(2, node4, node5), TreeNode(3, node6, node5))
twoStackLeft = TreeNode(1, TreeNode(2, node4, node5), TreeNode(3, node6, node7))
print(compare(twoStackRight, twoStackLeft))