import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "Hello world!", None)
        self.assertEqual(node.to_html(), "<p>Hello world!</p>")

        node1 = LeafNode("a", "Click here", {"href" : "https://www.google.com/"})
        self.assertEqual(node1.to_html(), "<a href=\"https://www.google.com/\">Click here</a>")

        node2 = LeafNode("h1", "Heading 1", None)
        self.assertEqual(node2.to_html(), "<h1>Heading 1</h1>")

if __name__ == "__main__":
    unittest.main()