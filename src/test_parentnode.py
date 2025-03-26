import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )
    
    def test_mult_parents_children(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        child_node2 = LeafNode("i", "Hello, world!")
        parent_node = ParentNode("div", [child_node, child_node2])
        parent_node2 = ParentNode("section", [parent_node])
        self.assertEqual(
        parent_node2.to_html(),
        "<section><div><span><b>grandchild</b></span><i>Hello, world!</i></div></section>",
    )

    def test_no_children(self):
        parent_node = ParentNode("p", None, {"id": "test"})
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "No Children")

    def test_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("a", "click me", {"href": "www.test.com"})], {"id": "test"})
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "No Tag")

if __name__ == "__main__":
    unittest.main()