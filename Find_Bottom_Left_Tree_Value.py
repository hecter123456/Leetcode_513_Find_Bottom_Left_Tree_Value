import unittest

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNullRoot(self):
        root = None
        self.assertEqual(Solution.findBottomLeftValue(self,root),None);
    def testCompleteBinaryTree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertEqual(Solution.findBottomLeftValue(self,root),1);

class Solution():
    def findBottomLeftValue(self, root):
        if(root is None):
            return None
        if(root.left is None):
            return root.val
        else:
            return Solution.findBottomLeftValue(self,root.left)

if __name__ == '__main__':
    unittest.main()
