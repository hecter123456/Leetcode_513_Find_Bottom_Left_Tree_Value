import unittest

class unitest(unittest.TestCase):
    def testNullRoot(self):
        root = []
        self.assertEqual(Solution.findBottomLeftValue(self,root),None);

class Solution():
    def findBottomLeftValue(self, root):
        if(root is None):
            return None

if __name__ == '__main__':
    unittest.main()
