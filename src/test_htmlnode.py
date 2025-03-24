import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<a>", "Open Google", None, {"target" : "_blank"})
        self.assertEqual(node.__repr__(), "tag: <a>, value: Open Google, children: None, props: {'target': '_blank'}")

        node2 = HTMLNode("<p>", "Hello world", [node], None)
        self.assertEqual(node2.__repr__(), f"tag: <p>, value: Hello world, children: [{node}], props: None")



if __name__ == "__main__":
    unittest.main()