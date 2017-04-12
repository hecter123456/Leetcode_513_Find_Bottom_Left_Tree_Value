import unittest
from operator import itemgetter

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNullRoot(self):
        root = None
        self.assertEqual(Solution().findBottomLeftValue(root),None);
    def testCompleteBinaryTree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(Solution().findBottomLeftValue(root),1);
    def testBinaryTree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(4)
        self.assertEqual(Solution().findBottomLeftValue(root),5);

class Solution:
    def findBottomLeftValue(self, root):
        if(root is None):
            return None
        return self.DFS(root)[1]
    def DFS(self, root):
        if(root is None):
            return (-1,0)
        lis = [self.DFS(root.left),self.DFS(root.right),(0, root.val)]
        (x,y) = max(lis,key=lambda item:item[0])
        return (x+1,y)

if __name__ == '__main__':
    unittest.main()
